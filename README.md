# COMP4710_Forecasting and Applying Data Mining to Energy Consumption Based on Weather Data in Ontario
This README aims to provide guidance on how to run our machine learning models and neural network models to detect energy consumption results, and to obtain the 31 unique frequent patterns mentioned in our paper through the Apriori algorithm.

***
## **List of Contents** 
* [Prerequisites](#Prerequisites)
* [Data Mining Part](#Data-Mining)
* [Prediction Part](#Prediction)
    * [Machine Learning Models](#Machine-Learning-Models)
    * [The Neural Network Model](#The-Neural-Network-Model)
* [Resource](#Resource)
* [Acknowledgments](#Acknowledgments)
***
## Prerequisites

### Data Mining:

#### Required Library:
pandas, numpy, mlxtend 
***

### Prediction:

#### Installing Jupyter Notebook
Jupyter notebook is required for running the code of machine learning models and the neural network model.

**Python 3 is being used in Jupyter Notebook**

#### Required Library:
sklearn, pandas, numpy, seaborn, matplotlib, tensorflow, keras
***

## Data Mining Part:

### Frequent Patterns:
frequentItemSets.csv

### Association Rules:
Rules.csv

***

## Prediction Part:

### Machine Learning Models:
ML.ipynb

### The Neural Network Model:
LSTM.ipynb

***

## Resource
We went through the sources of "Hourly Demand" and "Hourly Weather" and merged them into a single file named "hourly electricity consumption in Ontario", which encapsulates the weather data and corresponding hourly energy consumption from 2003 to 2016 (Ontario_preprocess.ipynb).

[Raw Dataset](https://ssc.ca/en/case-study/predicting-hourly-electricity-demand-ontario)

***

## Acknowledgments
### Group Members
- Nathan Giesbrecht
- Daniel Mai
- Owen Hnylycia
- Junyi Lu
