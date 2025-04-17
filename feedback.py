import streamlit as st
import pandas as pd

st.title("💬 User Feedback")

name = st.text_input("Your Name")
feedback = st.text_area("Your Feedback")
if st.button("Submit"):
    with open("feedback.txt", "a") as f:
        f.write(f"{name}: {feedback}\n")
    st.success("Thank you for your feedback!")
