# Overview
This project is a Machine Learning (ML) model designed to predict how much a customer spends on e-commerce websites, specifically in the category of clothing and accessories. The model leverages customer data, browsing history, purchasing behavior, and other relevant features to estimate the expected amount a customer will spend during their shopping session.

# Objective
The main goal of this model is to predict how much a customer will spend based on their shopping session time on both the webiste and the application.

# Features
The model uses session data of the customer, including:

Session Data: Time spent on the website, Time on the application, Length of the membership 
Purchase History: Yearly Amount Spent by the customer
This model is built using the following techniques:

# Data Preprocessing:

Handle missing values

# Model Training:

Algorithms: I've used Linear Regression as the machine learning algorithm for model training.
Evaluation Metrics: RMSE (Root Mean Square Error), MAE (Mean Absolute Error), MSE (Mean Square Error)

# How to Run the Model
To run this project, ensure you have the following prerequisites installed:

Prerequisites:
Python 3.x
Required libraries:
pandas
numpy
scikit-learn
matplotlib
seaborn
Steps:
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt

# Prepare the dataset:

Place your dataset in the data/ folder.
The model expects the dataset in CSV format with the following structure:

Avg. Session Length	- Should be a float value calculated in hours
Time on App	- Should be a float value calculated in hours
Time on Website	- Should be a float value calculated in hours
Length of Membership - Should be a float value calculated in years	

# About the dataset:
This dataset is having data of customers who buys clothes online. The store offers in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.

The company is trying to decide whether to focus their efforts on their mobile app experience or their website.

# Model Performance
The performance of the model is evaluated using the following metrics:

RMSE (Root Mean Square Error): Measures the difference between actual spending and predicted spending.
MSE (Mean Squared Error): Indicates how well the independent variables explain the variability in spending behavior.
MAE (Mean Absolute Error): Average absolute difference between the predicted and actual spending amounts.
Results:
Training RMSE: 10.360075336805268
Testing RMSE: 8.832497852574932
Training MAE: 8.215875866653251
Testing MAE: 7.103600193221979

# File Structure

├── data/
│   └── Ecommerce Customers.csv   # Input dataset
├── models/
│   └── model.pkl                 # Trained model
├── notebooks/
│   └── EDA.ipynb                 # Exploratory Data Analysis
├── requirements.txt              # List of dependencies
└── README.md                     # Project documentation

# Contact
For any questions or support, please reach out to:

Name: Hitesh Matharu
Email: hitesh04matharu@gmail.com
GitHub: HiteshM30