import openai

def generate_bullets(task, jd):
    prompt = f"""
    Rewrite the following task as a strong resume bullet point using Action + Task + Result format. Make it relevant to the job:
    Task: {task}
    Job Description: {jd}
    Give 3 variations.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip().split("\n")