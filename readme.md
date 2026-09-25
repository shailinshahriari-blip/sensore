# Home Occupancy Prediction

This project uses Machine Learning to predict whether a person is present in a house or not.

## About the Project

The goal of this project is to detect whether a house is occupied by using environmental and sensor data.

The model uses information collected from different sensors and predicts whether someone is present in the house.

## Input Features

The model uses the following features:

- Temperature
- Humidity
- Light
- CO2
- HR

## Target

The target variable is Occupancy.

- 1 → A person is present in the house.
- 0 → No person is present in the house.

## Machine Learning Model

The model is trained using the sensor data and learns the relationship between the input features and the Occupancy value.

After training, the model can predict the Occupancy for new data.

## Project Workflow

1. Load the dataset.
2. Select the input features.
3. Select Occupancy as the target.
4. Split the data into training and testing sets.
5. Train the Machine Learning model.
6. Make predictions on the test data.
7. Calculate the accuracy.
8. Save the results in an Excel file.

## Model Accuracy

Accuracy: YOUR_ACCURACY_HERE%

## Results

The results of the model are saved in an Excel file.

The Excel file contains the predicted Occupancy values.

- 1 → Occupied
- 0 → Unoccupied

## Results Image

![Model Results] (predict.png)

## Conclusion

This project demonstrates how Machine Learning can be used with environmental sensor data to detect whether a house is occupied.

Using Temperature, Humidity, Light, CO2, and HR, the model predicts whether the house is occupied or unoccupied.