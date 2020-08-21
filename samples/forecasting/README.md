run the notebooks in order

01-process.ipynb

This notebook illustrates how to fill the time series with missing timeslots, remove outliers, and aggregate the data to handle the respective seasonality for different forecasting granularity -

hourly patterns repeated daily
daily patterns repeated weekly
monthly patterns repeated yearly

02-arima.ipynb

explore how to test stationarity, and if data is not stationary, how to remove trend and seasonality to forecast on the residual and then add trend and seasonality back in the forecast.

Determining the parameters for ARIMA requires a lot of trial and error, even with the help of ACF (auto correlation function) and PACF (partial auto correlation function) graphs. Auto ARIMA tries different parameters automatically and often produces much better results with far less effort. It's also not necessary to make the data stationary for Auto ARIMA.

03-ml-ipynb

With machine learning, we transform the data out of the timeseries domain into, for example, regression problems. It's not necessary to convert data to stationary for machine learning. This Jupyter notebook explores Random Forest for forecasting by manually adding features such as lags and day of week. The sample dataset does include weather data which is often very helpful in this type of forecasting. We didn't use weather data in this case because we want to mimic datasets that don't have weather data available.

Azure AutoML forecasting is capable of fitting different ML models and choosing the best model with stack or voting ensemble. It's also not necessary to manually calcuate the lags for AutoML.