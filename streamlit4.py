import streamlit as st




st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose an option",
    ["Home", "About", "Contact"]
)

st.sidebar.button("Submit")


st.title("My Streamlit App")

with st.sidebar:
    st.header("Settings")

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100)

if name:
    st.write(f"Hello, {name}!")
    st.write(f"Your age is {age}.")

#
# # use with st.sidebar: when you have multiple widgets:
with st.sidebar:
    st.title("Menu")
    option = st.selectbox("Choose", ["A", "B", "C"])
    value = st.slider("Value", 0, 100, 50)