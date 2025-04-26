# cover_letter/generator.py

def generate_cover_letter(name, job_title, company, skills, voice="default"):
    skills_str = ", ".join(skills)
    intro = {
        "default": f"My name is {name}, and I’m excited to apply for the {job_title} role at {company}.",
        "enthusiastic": f"I’m thrilled to express interest in the {job_title} position at {company}."
    }

    body = (
        f"With a background in {skills_str}, I bring valuable experience aligned with the responsibilities "
        f"of this role. I’m eager to contribute to your team’s ongoing success."
    )

    return f"""
Dear {company} Hiring Team,

{intro.get(voice, intro['default'])}
{body}

Thank you for your consideration.
Sincerely,
{name}
"""