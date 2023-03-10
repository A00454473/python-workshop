import streamlit as st
from joblib import load

st.title("Iris prediction")
LABELS = ['setosa', 'versicolor', 'virginica']

clf = load("DT.joblib")

sp_l = st.slider('sepal length (cm)', min_value=0, max_value=10)
sp_w = st.slider('sepal width (cm)', min_value=0, max_value=10)
pe_l = st.slider('petal length (cm)', min_value=0, max_value=10)
pe_w = st.slider('petal width (cm)', min_value=0, max_value=10)

pred = clf.predict([[sp_l, sp_w, pe_l, pe_w]])
print(pred)

st.write(LABELS[pred[0]])