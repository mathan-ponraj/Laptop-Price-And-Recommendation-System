import streamlit as st
import pandas as pd
import joblib

# Load model and dataset
model = joblib.load("model/model.pkl")
df = pd.read_csv("data/data.csv")

st.title("💻 Laptop Recommendation System")

# User input filters
budget = st.slider("Select your budget (₹)", 10000, 150000, 50000)
brand = st.selectbox("Preferred Brand", ['Any'] + df['Brand'].unique().tolist())
ram = st.selectbox("Minimum RAM (GB)", sorted(df['RAM_GB'].unique()))
storage = st.selectbox("Minimum Storage (GB)", sorted(df['Storage'].unique()))
storage_type = st.selectbox("Storage Type", ['Any'] + df['Storage_type'].unique().tolist())

# Filter logic
filtered_df = df[df['Price'] <= budget]
if brand != 'Any':
    filtered_df = filtered_df[filtered_df['Brand'] == brand]
if storage_type != 'Any':
    filtered_df = filtered_df[filtered_df['Storage_type'] == storage_type]
filtered_df = filtered_df[filtered_df['RAM_GB'] >= ram]
filtered_df = filtered_df[filtered_df['Storage'] >= storage]

# Predict
if not filtered_df.empty:
    X = filtered_df[['Processor_name', 'OS', 'Brand','RAM_GB', 'Storage', 'Price']]  # change if you used more features
    predictions = model.predict(X)
    filtered_df['Predicted Score'] = predictions
    top_laptops = filtered_df.sort_values('Predicted Score', ascending=False).head(5)

    st.subheader("🎯 Top Laptop Recommendations")
    st.dataframe(top_laptops[['Name','Processor_name', 'OS', 'Brand','RAM_GB', 'Storage', 'Price']])
   
    st.download_button("📥 Download CSV", top_laptops.to_csv(index=False), "recommendations.csv", "text/csv")
else:
    st.warning("⚠️ No laptops found for the selected criteria.")
