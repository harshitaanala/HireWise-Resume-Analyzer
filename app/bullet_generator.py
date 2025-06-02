from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_bullets(task, jd):
    prompt = f"""
    Rewrite the following task as a strong resume bullet point using Action + Task + Result format. Make it relevant to the job:
    Task: {task}
    Job Description: {jd}
    Give 3 variations.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    # Split the output by new lines and filter out empty lines
    bullets = [line.strip() for line in response.choices[0].message.content.strip().split("\n") if line.strip()]
    return bullets
