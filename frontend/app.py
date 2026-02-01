import streamlit as st
import requests
import json

API = "http://localhost:8000"

st.title("Renewable Energy Site Finder")

query = st.text_input("Describe your renewable energy project")

if st.button("Run analysis"):
    req = requests.post(f"{API}/parse", params={"query": query}).json()
    st.subheader("Parsed requirements")
    st.json(req)

    res = requests.post(f"{API}/analyze", json=req).json()
    st.subheader("Top sites")
    st.map(res["sites"])

