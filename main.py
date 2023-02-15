import streamlit as st
from joblib import load

st.title("Main")

clf = load("DT.joblib")