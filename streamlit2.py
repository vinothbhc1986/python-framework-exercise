import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

if st.button("Add"):
    st.write("Result:", a + b)