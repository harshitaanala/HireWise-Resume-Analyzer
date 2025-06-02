import re

def get_ats_score(resume_text, jd_text):
    jd_keywords = set(re.findall(r'\b\w+\b', jd_text.lower()))
    resume_keywords = set(re.findall(r'\b\w+\b', resume_text.lower()))
    match = jd_keywords.intersection(resume_keywords)
    score = (len(match) / len(jd_keywords)) * 100
    return round(score, 2)