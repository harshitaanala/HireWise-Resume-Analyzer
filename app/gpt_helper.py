from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume_with_gpt(resume, jd):
    prompt = f"""
    Given the following resume and job description, analyze the match:
    Resume: {resume}
    Job Description: {jd}
    Provide:
    1. Skills matched
    2. Missing keywords
    3. Suggestions to improve
    Format as bullet points.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
