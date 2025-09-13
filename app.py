import streamlit as st
import pandas as pd
import os

st.title("InternMatch – Smart Internship Recommendation Engine")

# ✅ Load Member 1's dataset
data_path = "internship_dataset.csv"

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.success(f"✅ Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
else:
    st.error("❌ Dataset not found! Please add 'internship_dataset.csv' in /data folder.")
    st.stop()

# 🟢 Clean column names to avoid issues with spaces
df.columns = [col.strip() for col in df.columns]

# Input Form
st.header("Enter Your Details")

education = st.selectbox("Education", sorted(df["Education"].dropna().unique()))
skills = st.text_input("Skills (comma separated, e.g. Python, Excel)")
location = st.selectbox("Preferred Location", sorted(df["location Preference"].dropna().unique()))
interest = st.selectbox("Sector Interest", sorted(df["Sector Interest"].dropna().unique()))

# Submit Button
if st.button("Submit"):
    st.subheader("✅ Your Input")
    st.write("**Education:**", education)
    st.write("**Skills:**", skills)
    st.write("**Location:**", location)
    st.write("**Sector Interest:**", interest)

    # ✅ Show first few rows to confirm connection
    st.subheader("📂 Internship Data Preview")
    st.write(df.head())
