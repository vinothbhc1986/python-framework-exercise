import streamlit as st

st.markdown("""
# Hello Streamlit 👋

This is **bold text** and this is *italic text*.

### Features
- Easy to use
- Supports **Markdown**
- Great for data apps

[Visit Streamlit](https://streamlit.io/)
""")
# st.markdown() supports standard Markdown such as headings, bold, italics, lists, links, code, tables, and blockquotes.

st.markdown(
    "<h1 style='color:blue;'>Hello Streamlit!</h1>",
    unsafe_allow_html=True
)