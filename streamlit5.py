import streamlit as st
import requests

st.set_page_config(
    page_title="API Dashboard",
    layout="wide"
)

def check_api(url: str) -> tuple[bool, str]:
    try:
        response = requests.get(url, timeout=3)

        if response.ok:
            return True, f"Online ({response.status_code})"
        return False, f"Error ({response.status_code})"

    except requests.RequestException:
        return False, "Offline"


# Sidebar
with st.sidebar:
    st.header("API Status")

    api_url = "https://reqres.in/api/users?page=1"  #https://reqres.in/api/users?page=1

    is_online, status = check_api(api_url)

    if is_online:
        st.success(f"🟢 {status}")
    else:
        st.error(f"🔴 {status}")

    st.caption(f"Endpoint: `{api_url}`")


# Main application
st.title("Dashboard")
st.write("Application content goes here.")