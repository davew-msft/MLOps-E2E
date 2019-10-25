import argparse
import os
import pandas as pd
import numpy as np
import json

import keras
from keras import models 
from keras import layers
from keras import optimizers
import azureml.core
from azureml.core import Run
from azureml.core.model import Model

print("In train.py")
print("As a data scientist, this is where I write my training code.")

parser = argparse.ArgumentParser("train")

parser.add_argument("--model_name", type=str, help="model name", dest="model_name", required=True)
parser.add_argument("--build_number", type=str, help="build number", dest="build_number", required=True)

args = parser.parse_args()

print("Argument 1: %s" % args.model_name)
print("Argument 2: %s" % args.build_number)

def get_data():
    data_url = ('https://quickstartsws9073123377.blob.core.windows.net/'
                'azureml-blobstore-0d1c4218-a5f9-418b-bf55-902b65277b85/'
                'quickstarts/connected-car-data/connected-car_components.csv')
    car_components_df = pd.read_csv(data_url)
    components = car_components_df["text"].tolist()
    labels = car_components_df["label"].tolist()
    return { "components" : components, "labels" : labels }

def download_glove():
    print("Downloading GloVe embeddings...")
    import urllib.request
    glove_url = ('https://quickstartsws9073123377.blob.core.windows.net/'
                 'azureml-blobstore-0d1c4218-a5f9-418b-bf55-902b65277b85/'
                 'quickstarts/connected-car-data/glove.6B.100d.txt')
    urllib.request.urlretrieve(glove_url, 'glove.6B.100d.txt')
    print("Download complete.")

download_glove()

# Load the car components labeled data
print("Loading car components data...")
data_url = ('https://quickstartsws9073123377.blob.core.windows.net/'
            'azureml-blobstore-0d1c4218-a5f9-418b-bf55-902b65277b85/'
            'quickstarts/connected-car-data/connected-car_components.csv')
car_components_df = pd.read_csv(data_url)
components = car_components_df["text"].tolist()
labels = car_components_df["label"].tolist()
print("Loading car components data completed.")

# split data 60% for trianing, 20% for validation, 20% for test
print("Splitting data...")
train, validate, test = np.split(car_components_df.sample(frac=1), [int(.6*len(car_components_df)), int(.8*len(car_components_df))])
print(train.shape)
print(test.shape)
print(validate.shape)

# use the Tokenizer from Keras to "learn" a vocabulary from the entire car components text
print("Tokenizing data...")
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

maxlen = 100                                           
training_samples = 90000                                 
validation_samples = 5000    
max_words = 10000      

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(components)
sequences = tokenizer.texts_to_sequences(components)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=maxlen)

labels = np.asarray(labels)
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

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
print("Tokenizing data complete.")

# apply the vectors provided by GloVe to create a word embedding matrix
print("Applying GloVe vectors...")
glove_dir =  './'

embeddings_index = {}
f = open(os.path.join(glove_dir, 'glove.6B.100d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

embedding_dim = 100

embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    if i < max_words:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector    
print("Applying GloVe vectors compelted.")

# use Keras to define the structure of the deep neural network   
print("Creating model structure...")
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# fix the weights for the first layer to those provided by the embedding matrix
model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False
print("Creating model structure completed.")

opt = optimizers.RMSprop(lr=0.1)

print("Training model...")
model.compile(optimizer=opt,loss='binary_crossentropy', metrics=['acc'])
model.fit(x_train, y_train, epochs=1, batch_size=32, validation_data=(x_val, y_val))
print("Training model completed.")

print("Saving model files...")
# create a ./outputs folder in the compute target
os.makedirs('./outputs', exist_ok=True)
# save model
model.save('./outputs/model.h5')
print("model saved in ./outputs folder")
print("Saving model files completed.")

print('Model evaluation will print the following metrics: ', model.metrics_names)
evaluation_metrics = model.evaluate(x_test, y_test)
print(evaluation_metrics)

run = Run.get_context()
run.log(model.metrics_names[0], evaluation_metrics[0], 'Model test data loss')
run.log(model.metrics_names[1], evaluation_metrics[1], 'Model test data accuracy')

os.chdir("./outputs")

model_description = 'Deep learning model to classify the descriptions of car components as compliant or non-compliant.'
model = Model.register(
    model_path='model.h5',  # this points to a local file
    model_name=args.model_name,  # this is the name the model is registered as
    tags={"type": "classification", "run_id": run.id, "build_number": args.build_number},
    description=model_description,
    workspace=run.experiment.workspace
)

os.chdir("..")

print("Model registered: {} \nModel Description: {} \nModel Version: {}".format(model.name, 
                                                                                model.description, model.version))





