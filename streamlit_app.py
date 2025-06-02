import streamlit as st
from app.main import run_app
from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Load environment variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY") 
mongo_uri = os.getenv("MONGO_URI") 

st.set_page_config(page_title="HireWise – Resume Optimizer", layout="wide")

st.title("📄 HireWise – AI Resume Analyzer")

# Directly run the main app without login/signup
run_app()
