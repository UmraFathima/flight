Airway Customer Satisfaction Prediction

This repository contains a machine learning project aimed at predicting the satisfactory level of customers for an airways company. The project utilizes the Django framework for backend development, with Python as the primary backend language. For frontend development, HTML and CSS are used. The model is trained using a dataset sourced from a .csv file.

Project Overview

The goal of this project is to develop a predictive model that can determine the satisfaction level of customers for an airways company based on various features. The project involves data preprocessing, model training using the Support Vector Machine (SVM) algorithm, and deployment using Django.

Technologies Used

Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Python: A versatile programming language commonly used for web development, data analysis, and machine learning.
HTML/CSS: Frontend technologies used for creating user interfaces and styling web pages.
Pandas: A powerful data manipulation library in Python used for data preprocessing and analysis.
Scikit-learn: A machine learning library in Python that provides simple and efficient tools for data mining and data analysis.

Dataset

The training dataset used for this project is sourced from a .csv file. It contains various features related to customer interactions and satisfaction levels with an airways company. Model Training

The predictive model is trained using the Support Vector Machine (SVM) algorithm, a supervised learning method commonly used for classification tasks. Additionally, the data is scaled using StandardScaler from Scikit-learn to improve model accuracy. Model Evaluation

The accuracy of the predictive model is deemed to be good, achieved through rigorous training and validation processes. Usage

To run this project locally:

Clone the repository:

bash

git clone https://github.com/yourusername/airway-customer-satisfaction.git

Install the required dependencies:

pip install -r requirements.txt

Navigate to the project directory and run the Django server:

bash

cd airway-customer-satisfaction python manage.py runserver

Access the application in your web browser at http://localhost:8000
![image](https://github.com/UmraFathima/flight/assets/154687173/b7464618-09f4-40d0-b9d6-2362d479e72e)
