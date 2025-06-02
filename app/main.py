import streamlit as st
from app.resume_parser import extract_text_from_pdf
from app.ats_score import get_ats_score
from app.gpt_helper import analyze_resume_with_gpt
from app.bullet_generator import generate_bullets

def run_app():
    st.sidebar.header("Upload Section")
    resume_file = st.sidebar.file_uploader("Upload Resume (PDF only)", type=["pdf"])
    jd_input = st.sidebar.text_area("Paste Job Description")

    if resume_file and jd_input:
        resume_text = extract_text_from_pdf(resume_file)

        st.subheader("📊 ATS Score")
        score = get_ats_score(resume_text, jd_input)
        st.metric("ATS Score", f"{score}%")

        st.subheader("🤖 GPT Suggestions")
        suggestions = analyze_resume_with_gpt(resume_text, jd_input)
        st.write(suggestions)

        st.subheader("✍️ Improve My Bullet Point")
        task_input = st.text_input("Enter your task")
        if task_input:
            new_bullets = generate_bullets(task_input, jd_input)
            for bullet in new_bullets:
                st.markdown(f"- {bullet}")