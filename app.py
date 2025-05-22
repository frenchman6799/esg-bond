import streamlit as st
import pandas as pd

st.title("🇮🇳 India ESG Bond Dashboard")
st.write("Auto-loading SEBI data...")

# Load sample data (we'll replace this later)
data = pd.DataFrame({
    "Issuer": ["L&T Finance", "IREDA"],
    "Amount (₹ Cr)": [667, 275],
    "Coupon (%)": [7.59, 8.51]
})
st.dataframe(data)
