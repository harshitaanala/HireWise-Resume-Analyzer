# app/auth.py

import streamlit as st
import bcrypt
from pymongo import MongoClient
import os

# Load from Streamlit secrets or environment
mongo_uri = os.getenv("MONGO_URI") or st.secrets["MONGO_URI"]
client = MongoClient(mongo_uri)
db = client["hirewise"]  # Change DB name if needed
users_collection = db["users"]


def login():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = users_collection.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            st.success("Login successful!")
            st.session_state.authenticated = True
            st.session_state.username = username
        else:
            st.error("Invalid credentials")


def signup():
    st.subheader("📝 Sign Up")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type='password')
    confirm = st.text_input("Confirm Password", type='password')

    if st.button("Sign Up"):
        existing_user = users_collection.find_one({"username": username})
        if existing_user:
            st.warning("Username already exists.")
        elif password != confirm:
            st.error("Passwords do not match")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users_collection.insert_one({
                "username": username,
                "password": hashed_password
            })
            st.success("Account created! Please login.")
