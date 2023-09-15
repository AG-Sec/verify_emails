import streamlit as st
import csv
import pandas as pd
from validate_email import validate_email

upload = st.file_uploader("Upload a CSV file - No header row")

def validate(data):
    address = data
    results = []
    
    is_valid = validate_email(address,verify=True)
    results.append(f"{address} - {str(is_valid)}")

    return results

if upload is not None:
    df = pd.read_csv(upload, header=None)
    res=[]
    for a in df[0]:
        v = validate(a)
        res.append(v)
    st.table(res)

