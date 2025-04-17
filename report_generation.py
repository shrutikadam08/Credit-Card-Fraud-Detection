import streamlit as st
import pandas as pd

st.title("📄 Report Generation")

generated_df = st.session_state.get("generated_df", None)

if generated_df is not None:
    st.write("Preview Report:")
    st.dataframe(generated_df)
    csv = generated_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Report", csv, "fraud_predictions.csv", "text/csv")
else:
    st.warning("No predictions found to generate report. Go to Predict tab first.")