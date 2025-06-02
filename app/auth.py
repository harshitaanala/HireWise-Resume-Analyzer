import streamlit as st

def login():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.authenticated = True
        else:
            st.error("Invalid credentials")

def signup():
    st.subheader("📝 Sign Up")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type='password')
    confirm = st.text_input("Confirm Password", type='password')
    if st.button("Sign Up"):
        if password == confirm:
            st.success("Account created! Please login.")
        else:
            st.error("Passwords do not match")