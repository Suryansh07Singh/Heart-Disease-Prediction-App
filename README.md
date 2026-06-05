# ❤️ Heart Disease Prediction App

A Machine Learning-powered web application built with Streamlit that predicts the likelihood of heart disease based on patient health parameters. The project involves data preprocessing, exploratory analysis, model training, evaluation, and deployment of the best-performing model.

---

## 📌 Project Overview

Cardiovascular diseases are among the leading causes of death worldwide. Early prediction and diagnosis can help reduce risks and improve patient outcomes.
This project uses Machine Learning classification algorithms to analyze patient health data and predict whether a person is at risk of heart disease. Multiple models were trained and compared to identify the most effective algorithm.
The final application provides an easy-to-use web interface where users can input health-related parameters and receive instant predictions.

---

## 🎯 Objectives

* Build a Machine Learning model for heart disease prediction.
* Perform data cleaning and preprocessing.
* Compare the performance of multiple classification algorithms.
* Select the best-performing model based on evaluation metrics.
* Deploy the model using Streamlit for real-time predictions.

---

## 📊 Dataset

Dataset Used: **heart-checkpoint.csv**

The dataset contains various medical attributes associated with heart disease diagnosis.

### Features Used

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG Results
* Maximum Heart Rate Achieved
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* Slope of Peak Exercise ST Segment
* Number of Major Vessels
* Thalassemia
* Target Variable (Heart Disease Presence)

> Note: Feature names may vary depending on the dataset version used.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed before model training:

### 1. Data Cleaning

* Removed duplicate records.
* Checked dataset consistency.
* Verified data types.

### 2. Handling Missing Values

* Identified null or missing values.
* Removed or appropriately handled missing records.

### 3. Feature Scaling

Standardization was applied using **StandardScaler** to normalize feature values.

Benefits:

* Improves model performance.
* Ensures all features contribute equally.
* Particularly useful for distance-based algorithms such as KNN and SVM.

### 4. Train-Test Split

The dataset was divided into:

* Training Set
* Testing Set

This ensures unbiased model evaluation.

---

## 🤖 Machine Learning Models Used

Five classification algorithms were trained and evaluated:

### 1. Logistic Regression

* Linear classification algorithm.
* Efficient and interpretable.
* Achieved the highest accuracy among all tested models.
* Selected as the final deployment model.

### 2. K-Nearest Neighbors (KNN)

* Instance-based learning algorithm.
* Classifies data based on neighboring points.
* Performance depends on the value of K.

### 3. Decision Tree

* Tree-based classification model.
* Easy to interpret and visualize.
* May overfit if not properly controlled.

### 4. Naive Bayes

* Probabilistic classifier based on Bayes' Theorem.
* Fast and computationally efficient.
* Works well on smaller datasets.

### 5. Support Vector Machine (SVM)

* Powerful classification algorithm.
* Effective for high-dimensional data.
* Often provides strong classification performance after feature scaling.

---

## 📈 Model Evaluation

The models were compared using classification performance metrics such as:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Model Comparison

| Model               | Purpose                      |
| ------------------- | ---------------------------- |
| Logistic Regression | Final Model                  |
| KNN                 | Benchmark Comparison         |
| Decision Tree       | Rule-Based Classification    |
| Naive Bayes         | Probabilistic Classification |
| SVM                 | Margin-Based Classification  |

### Best Performing Model

🏆 **Logistic Regression**

The Logistic Regression model achieved the highest prediction accuracy and was selected for deployment in the Streamlit application.

---

## 🖥️ Streamlit Application

The web application allows users to:

* Enter patient health information.
* Submit values for prediction.
* Receive real-time heart disease risk predictions.
* Interact with a simple and user-friendly interface.

### Application Workflow

1. User enters health parameters.
2. Input data is preprocessed.
3. Logistic Regression model processes the data.
4. Prediction result is displayed.
5. User receives risk assessment instantly.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

### Development Tools

* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
Heart-Disease-Prediction-App/
│
├── app.py
├── heart-checkpoint.csv
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd Heart-Disease-Prediction-App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📋 Future Improvements

* Hyperparameter tuning for improved accuracy.
* Addition of ensemble learning models.
* Integration with cloud databases.
* Enhanced visualization dashboard.

---

## 📚 Learning Outcomes

Through this project, the following concepts were applied:

* Data Cleaning
* Feature Engineering
* Feature Scaling
* Classification Algorithms
* Model Evaluation
* Machine Learning Workflow
* Streamlit Deployment
* GitHub Project Management

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

Suryansh Vikram Singh

Machine Learning and Data Science Enthusiast focused on building practical AI-powered applications and solving real-world problems using data-driven solutions.
