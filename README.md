# Ideal Weight Prediction Model

This data science model is based on health data from the United States and aims to predict whether a person has their ideal weight or if they are underweight, overweight, or obese. The data was downloaded from kaggle.

The excersice is divided into two parts:
1) The creation of a machine learning model that is able to use for predictions.
2) A web app that allows the user to enter data for predictions.

## Structure

The project is organized as follows:

- `01_stats_descriptions.ipynb` - The descriptive analysis for the dataset.
- `02_exploratory_data_analysis.ipynb` - A notebook to explore the data, play around, visualize and clean it.
- `03_ml_develop.ipynb` - A notebook where the machine learning model is developed.
- `requirements.txt` - This file contains the list of necessary python packages.
- `app.py` - This file has the script to run the machine learning model in streamlit.
- `models/` - This directory contains the machine learning model.
- `data/` - This directory contains the following subdirectories:
  - `interin/` - For intermediate data that has been transformed.
  - `processed/` - For the final data to be used for modeling.
  - `raw/` - For raw data without any processing.
 
  

## Running the Web app

To run the webb app, please follow this link:

https://fourgeeks-streamlit-integration-1fti.onrender.com/

Next, enter your height and weight and click "predict" to see the results