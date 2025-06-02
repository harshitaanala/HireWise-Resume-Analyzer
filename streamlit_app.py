import streamlit as st
from app.auth import login, signup
from app.main import run_app

st.set_page_config(page_title="HireWise – Resume Optimizer", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.title("📄 HireWise – AI Resume Analyzer")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Choose an option", menu)

if not st.session_state.authenticated:
    if choice == "Login":
        login()
    else:
        signup()
else:
    run_app()