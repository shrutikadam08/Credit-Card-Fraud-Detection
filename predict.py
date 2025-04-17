import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


model = joblib.load("model/model.pkl")
merchant_encoder = joblib.load("model/merchant_encoder.pkl")
category_encoder = joblib.load("model/category_encoder.pkl")

st.title("👀 Predict Fraudulent Transactions")

option = st.radio("Choose input type", ("CSV Upload", "Manual Input"))

if option == "CSV Upload":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        input_df = pd.read_csv(uploaded_file)

       
        if 'merchant' in input_df.columns:
            input_df['merchant'] = merchant_encoder.transform(input_df['merchant'])
        if 'category' in input_df.columns:
            input_df['category'] = category_encoder.transform(input_df['category'])

       
        input_df = input_df[['amt', 'age', 'merchant', 'category', 'feature5', 'feature6', 'feature7', 'feature8', 'feature9']]

       
        pred = model.predict(input_df)
        input_df['is_fraud_predicted'] = pred
        st.write(input_df)
        st.success("Prediction completed")

elif option == "Manual Input":
    st.write("Enter the features manually:")

    col1, col2 = st.columns(2)
    with col1:
        amt = st.number_input("Amount", value=100.0)
        age = st.number_input("Age", value=30)
    with col2:
        merchant = st.text_input("Merchant Name", value="ABC")
        category = st.text_input("Category", value="shopping_pos")
        feature5 = st.number_input("Feature 5", value=0.0)
        feature6 = st.number_input("Feature 6", value=0.0)
        feature7 = st.number_input("Feature 7", value=0.0)
        feature8 = st.number_input("Feature 8", value=0.0)
        feature9 = st.number_input("Feature 9", value=0.0)

    if st.button("Predict"):
        
        merchant_encoded = merchant_encoder.transform([merchant])[0]
        category_encoded = category_encoder.transform([category])[0]

        
        new_df = pd.DataFrame({
            'amt': [amt],
            'age': [age],
            'merchant': [merchant_encoded],
            'category': [category_encoded],
            'feature5': [feature5],
            'feature6': [feature6],
            'feature7': [feature7],
            'feature8': [feature8],
            'feature9': [feature9]
        })

        
        pred = model.predict(new_df)
        st.write("Prediction:", "Fraud" if pred[0] == 1 else "Legit")
