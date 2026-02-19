# ❤️ Heart Disease Prediction System using Machine Learning

An end-to-end Machine Learning-based Heart Disease Prediction system developed as a Final Year Project (BS Mathematics, COMSATS University Islamabad).

This project uses real-world clinical data to predict the presence of heart disease using advanced machine learning techniques and provides real-time predictions through a Flask-based web application.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection can significantly reduce risks and improve treatment outcomes.

This project develops a complete ML pipeline that:

- Performs data preprocessing and exploratory data analysis
- Trains and compares multiple machine learning models
- Selects the best-performing model (XGBoost)
- Deploys the trained model in a web-based interface using Flask

---

## 📊 Dataset Information

- Publicly available heart disease dataset
- ~1300 patient records
- 13 clinical input attributes
- Binary classification problem:
  - 1 → Heart Disease Present
  - 0 → No Heart Disease

### Input Features Used:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression (Oldpeak)
- Slope of ST Segment
- Number of Major Vessels (CA)
- Thalassemia

---

## 🧠 Machine Learning Models Implemented

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Neural Network
- **XGBoost (Selected Best Model)**

### 🏆 Best Model: XGBoost

XGBoost achieved the highest accuracy and best balance between precision and recall, making it the final deployed model.

---

## ⚙️ Technologies & Tools Used

- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Flask
- Joblib
- Google Colab (Model Training)
- VS Code (Deployment)

---

## 🌐 Web Application

The trained XGBoost model is integrated into a Flask web application that:

- Accepts 13 clinical inputs from the user
- Processes input data
- Generates real-time heart disease prediction
- Displays risk result through a user-friendly interface

---

