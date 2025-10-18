import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import io

st.set_page_config(page_title="Kidney Disease Prediction", layout="centered")
st.title("Kidney Disease Prediction App")

@st.cache_data
def load_data():
    df = pd.read_csv("kidney_disease.csv")
    df.drop('id', axis=1, inplace=True)
    df.columns = [
        'age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells',
        'pus_cell', 'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea',
        'serum_creatinine', 'sodium', 'potassium', 'haemoglobin', 'packed_cell_volume',
        'white_blood_cell_count', 'red_blood_cell_count', 'hypertension', 'diabetes_mellitus',
        'coronary_artery_disease', 'appetite', 'peda_edema', 'aanemia', 'class'
    ]
    return df

@st.cache_data
def train_model(df):
    df = df.dropna()
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])
    X = df.drop("class", axis=1)
    y = df["class"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    return model, X.columns.tolist(), le

# Load and train
df = load_data()
model, feature_names, encoder = train_model(df)

st.subheader("Masukkan Data Anda:")
user_input = {}

for col in feature_names:
    if df[col].dtype == 'object':
        options = df[col].dropna().unique().tolist()
        user_input[col] = st.selectbox(col, options)
    else:
        min_val = df[col].min()
        max_val = df[col].max()
        mean_val = df[col].mean()
        user_input[col] = st.number_input(col, min_value=float(min_val), max_value=float(max_val), value=float(mean_val))

# Predict
if st.button("Prediksi Penyakit Ginjal"):
    input_df = pd.DataFrame([user_input])
    for col in input_df.select_dtypes(include='object').columns:
        input_df[col] = encoder.fit(df[col]).transform(input_df[col])
    prediction = model.predict(input_df)[0]
    result = "CKD (Chronic Kidney Disease)" if prediction == 1 else "Not CKD"
    st.success(f"Hasil Prediksi: {result}")
