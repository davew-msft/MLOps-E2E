import argparse
import json
import urllib

import os
import numpy as np
import pandas as pd

import keras
from keras import models 
from keras import layers
from keras import optimizers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

import azureml.core
from azureml.core import Run
from azureml.core.dataset import Dataset
from azureml.core.datastore import Datastore
from azureml.core.model import Model

print("Executing train.py")
print("As a data scientist, this is where I write my training code.")
print("Azure Machine Learning SDK version: {}".format(azureml.core.VERSION))

#-------------------------------------------------------------------
#
# Processing input arguments
#
#-------------------------------------------------------------------

parser = argparse.ArgumentParser("train")

parser.add_argument("--model_name", type=str, help="model name", dest="model_name", required=True)
parser.add_argument("--build_number", type=str, help="build number", dest="build_number", required=True)

args = parser.parse_args()

print("Argument 1: %s" % args.model_name)
print("Argument 2: %s" % args.build_number)

#-------------------------------------------------------------------
#
# Define internal variables
#
#-------------------------------------------------------------------

datasets_folder = './datasets'

# this is the URL to the CSV file containing the GloVe vectors
glove_url = ('https://quickstartsws9073123377.blob.core.windows.net/'
             'azureml-blobstore-0d1c4218-a5f9-418b-bf55-902b65277b85/'
             'quickstarts/connected-car-data/glove.6B.100d.txt')

glove_ds_name = 'glove_6B_100d'
glove_ds_description ='GloVe embeddings 6B 100d'

# this is the URL to the CSV file containing the connected car component descriptions
cardata_url = ('https://quickstartsws9073123377.blob.core.windows.net/'
            'azureml-blobstore-0d1c4218-a5f9-418b-bf55-902b65277b85/'
            'quickstarts/connected-car-data/connected-car_components.csv')

cardata_ds_name = 'connected_car_components'
cardata_ds_description = 'Connected car components data'

embedding_dim = 100                                        
training_samples = 90000                                 
validation_samples = 5000    
max_words = 10000

run = Run.get_context()
ws = run.experiment.workspace
ds = Datastore.get_default(ws)

#-------------------------------------------------------------------
#
# Process GloVe embeddings dataset
#
#-------------------------------------------------------------------

# The GloVe embeddings dataset is static so we will only register it once with the workspace

print("Downloading GloVe embeddings...")

try:
    glove_ds = Dataset.get_by_name(workspace=ws, name=glove_ds_name)
    print('GloVe embeddings dataset already registered.')
except:
    print('Registering GloVe embeddings dataset...')
    glove_ds = Dataset.File.from_files(glove_url)
    glove_ds.register(workspace=ws, name=glove_ds_name, description=glove_ds_description)
    print('GloVe embeddings dataset successfully registered.')
    
file_paths = glove_ds.download(target_path=datasets_folder, overwrite=True)
glove_file_path = file_paths[0]
print("Download complete.")

#-------------------------------------------------------------------
#
# Process connected car components dataset
#
#-------------------------------------------------------------------

print('Processing connected car components dataset...')

# Download the current version of the dataset and save a snapshot in the datastore
# using the build number as the subfolder name

local_cardata_path = '{}/connected-car-components.csv'.format(datasets_folder)
ds_cardata_path = 'datasets/{}'.format(args.build_number)

urllib.request.urlretrieve(cardata_url, local_cardata_path)
ds.upload_files([local_cardata_path], target_path=ds_cardata_path, overwrite=True)

cardata_ds = Dataset.Tabular.from_delimited_files(path=[(ds, 'datasets/{}/connected-car-components.csv'.format(args.build_number))])

# For each run, register a new version of the dataset and tag it with the build number.
# This provides full traceability using a specific Azure DevOps build number.

cardata_ds.register(workspace=ws, name=cardata_ds_name, description=cardata_ds_description,
    tags={"build_number": args.build_number}, create_new_version=True)
print('Connected car components dataset successfully registered.')

car_components_df = cardata_ds.to_pandas_dataframe()
components = car_components_df["text"].tolist()
labels = car_components_df["label"].tolist()

print("Processing car components data completed.")

#-------------------------------------------------------------------
#
# Use the Tokenizer from Keras to "learn" a vocabulary from the entire car components text
#
#-------------------------------------------------------------------

print("Tokenizing data...")    

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(components)
sequences = tokenizer.texts_to_sequences(components)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=embedding_dim)

labels = np.asarray(labels)
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)
print("Tokenizing data complete.")

#-------------------------------------------------------------------
#
# Create training, validation, and testing data
#
#-------------------------------------------------------------------

indices = np.arange(data.shape[0])  
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

x_train = data[:training_samples]
y_train = labels[:training_samples]

x_val = data[training_samples: training_samples + validation_samples]
y_val = labels[training_samples: training_samples + validation_samples]

x_test = data[training_samples + validation_samples:]
y_test = labels[training_samples + validation_samples:]

#-------------------------------------------------------------------
#
# Apply the vectors provided by GloVe to create a word embedding matrix
#
#-------------------------------------------------------------------

print("Applying GloVe vectors...")

embeddings_index = {}
f = open(glove_file_path)
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    if i < max_words:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector    
print("Applying GloVe vectors completed.")

#-------------------------------------------------------------------
#
# Build and train the model
#
#-------------------------------------------------------------------

# Use Keras to define the structure of the deep neural network   
print("Creating model structure...")

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=embedding_dim))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# fix the weights for the first layer to those provided by the embedding matrix
model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False
print("Creating model structure completed.")

opt = optimizers.RMSprop(lr=0.1)

print("Training model...")
model.compile(optimizer=opt,
              loss='binary_crossentropy',
              metrics=['acc'])
history = model.fit(x_train, y_train,
                    epochs=3, 
                    batch_size=32,
                    validation_data=(x_val, y_val))
print("Training model completed.")

print("Saving model files...")
# create a ./outputs/model folder in the compute target
# files saved in the "./outputs" folder are automatically uploaded into run history
os.makedirs('./outputs/model', exist_ok=True)
# save model
model.save('./outputs/model/model.h5')
print("model saved in ./outputs/model folder")
print("Saving model files completed.")

#-------------------------------------------------------------------
#
# Evaluate the model
#
#-------------------------------------------------------------------

print('Model evaluation will print the following metrics: ', model.metrics_names)
evaluation_metrics = model.evaluate(x_test, y_test)
print(evaluation_metrics)

run = Run.get_context()
run.log(model.metrics_names[0], evaluation_metrics[0], 'Model test data loss')
run.log(model.metrics_names[1], evaluation_metrics[1], 'Model test data accuracy')

#-------------------------------------------------------------------
#
# Register the model the model
#
#-------------------------------------------------------------------

os.chdir("./outputs/model")

# The registered model references the data set used to provide its training data

model_description = 'Deep learning model to classify the descriptions of car components as compliant or non-compliant.'
model = Model.register(
    model_path='model.h5',  # this points to a local file
    model_name=args.model_name,  # this is the name the model is registered as
    tags={"type": "classification", "run_id": run.id, "build_number": args.build_number},
    description=model_description,
    workspace=run.experiment.workspace,
    datasets=[('training data', cardata_ds), ('embedding data', glove_ds)])

print("Model registered: {} \nModel Description: {} \nModel Version: {}".format(model.name, 
                                                                                model.description, model.version))
