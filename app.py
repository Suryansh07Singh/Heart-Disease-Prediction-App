import streamlit as st
import pandas as pd
import joblib

model=joblib.load('LogReg.pkl')
scaler=joblib.load('scaler.pkl')
expected_columns=joblib.load('columns.pkl')

st.title("Heart Disease Prediction App by SURYANSH 💔")
st.markdown("This app predicts the likelihood of heart disease based on user input.")
age=st.slider("Age", 18, 100, 40)
sex=st.selectbox("Sex", ["Male", "Female"])
pain=st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
restbp=st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol=st.slider("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs=st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
resting_ecg=st.selectbox("Resting ECG", ["Normal", "ST", "LVM"])
max_heart_rate=st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina=st.selectbox("Exercise Induced Angina", [0,1])
oldpeak=st.slider("ST Depression Induced by Exercise", 0.0, 6.0, 1.0)
st_slope=st.selectbox("Slope of the Peak Exercise ST Segment", ["Up", "Flat", "Down"])

if st.button("Predict"):
    input_data = {
        'age': age,
        'Resting BP': restbp,
        'Cholesterol': chol,
        'Fasting BS': fbs,
        'Max HR': max_heart_rate,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'Chest Pain Type_' + pain: 1,
        'Resting ECG_' + resting_ecg: 1,
        'Exercise Angina_' + str(exercise_angina): 1,
        'ST Slope_' + st_slope: 1
    }
    input_df = pd.DataFrame([input_data])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("High Risk of Heart Disease. Please consult a healthcare professional for further evaluation.")
    else:
        st.success("Low Risk of Heart Disease. However, please maintain a healthy lifestyle and consult a healthcare professional for regular check-ups.")