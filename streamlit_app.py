import streamlit as st
from app.main import run_app
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # Load environment variables from .env

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

mongo_uri = os.getenv("MONGO_URI")

st.set_page_config(page_title="HireWise – Resume Optimizer", layout="wide")

st.title("📄 HireWise – AI Resume Analyzer")

# Pass the client if needed in run_app, else make client global/import it inside app files
run_app()
