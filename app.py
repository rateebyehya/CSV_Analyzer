import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

import os 

os.environ['OPENAI_API_KEY'] = "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"

st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

# Capture the CSV file
data = st.file_uploader("Upload CSV file",type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    # Get Response
    answer =  query_agent(data,query)
    st.write(answer)