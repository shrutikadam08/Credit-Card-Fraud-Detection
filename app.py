import streamlit as st
from PIL import Image
import requests
from io import BytesIO


st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection App")
st.markdown("""
Welcome to the Credit Card Fraud Detection web application. Navigate using the sidebar to:
- View data dashboards 
- Predict fraud transactions 
- Generate reports 
- Give your feedback
""")


