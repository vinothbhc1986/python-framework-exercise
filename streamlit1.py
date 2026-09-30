import streamlit as st

# Streamlit is a Python framework that lets you create interactive web applications using only Python.
st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")

#streamlit run streamlit1.py

