import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="Kidney Disease EDA", layout="wide")
st.title("Kidney Disease Data Analysis")

# File uploader
uploaded_file = st.file_uploader("Upload Kidney Disease CSV File", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df.drop('id', axis=1, inplace=True)
    df.columns = [
        'age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells',
        'pus_cell', 'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea',
        'serum_creatinine', 'sodium', 'potassium', 'haemoglobin', 'packed_cell_volume',
        'white_blood_cell_count', 'red_blood_cell_count', 'hypertension', 'diabetes_mellitus',
        'coronary_artery_disease', 'appetite', 'peda_edema', 'aanemia', 'class'
    ]
    return df

if uploaded_file is not None:
    df = load_data(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    buffer = []
    st.subheader("Dataset Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    st.subheader("Statistical Description")
    st.dataframe(df.describe())

    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.info("Please upload a CSV file to start.")
