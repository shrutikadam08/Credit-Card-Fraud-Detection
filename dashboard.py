import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

uploaded = st.file_uploader("Upload Dataset", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Fraud Count")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='is_fraud', data=df, ax=ax1, palette="Set2")
    st.pyplot(fig1)

    st.subheader("Fraud by Category")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.countplot(y=df[df['is_fraud'] == 1]['category'], 
                  order=df['category'].value_counts().index, ax=ax2)
    ax2.set_xlabel("Count")
    ax2.set_ylabel("Transaction Category")
    st.pyplot(fig2)

    st.subheader("Amount Distribution")
    fig3, ax3 = plt.subplots()
    sns.kdeplot(df[df['is_fraud'] == 0]['amt'], label="Legit", fill=True)
    sns.kdeplot(df[df['is_fraud'] == 1]['amt'], label="Fraud", fill=True)
    ax3.legend()
    st.pyplot(fig3)