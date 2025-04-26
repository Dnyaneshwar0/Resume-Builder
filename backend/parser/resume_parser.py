import re
def extract_section(text, header, next_headers):
    # Normalize input text to lower case and match headers in lowercase too
    header = header.lower()
    text = text.lower()
    next_headers = [nh.lower() for nh in next_headers]

    # Build dynamic regex to capture section until next header or end of text
    pattern = rf"{header}\s*(.*?)(?=\n(?:{'|'.join(next_headers)})\b|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else "N/A"

def extract_skills(skills_text):
    # Normalize and split on common delimiters
    raw = skills_text.replace('\n', ' ').replace('+', ',').replace(':', ',').lower()
    tokens = re.split(r'[,\n]', raw)

    keywords = []
    for token in tokens:
        token = token.strip()
        if not token or token in {"and", "or"}:
            continue
        # Extract from phrases like 'using puppet, ansible, chef'
        if "using" in token:
            token = token.split("using")[-1]
        keywords.extend(re.findall(r'\b[a-zA-Z0-9+#/.]+\b', token))

    return sorted(set(keywords))


def parse_resume(text):
    # Normalize text once
    text_lower = text.lower()

    # Extract name from first line (non-empty, before the first newline)
    name_line = text.split('\n')[0].strip()
    name_match = re.match(r'^[a-z ]+', name_line.lower())

    # Extract basic details
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text_lower)
    phone_match = re.search(r'(\+?\d[\d\s().-]{7,}\d)', text_lower)

    # Section extraction
    experience_text = extract_section(text, 'experience', ['education', 'skills'])
    education_text = extract_section(text, 'education', ['skills'])
    skills_text = extract_section(text, 'skills', [])

    resume_data = {
        'name': name_match.group().title() if name_match else 'N/A',
        'email': email_match.group() if email_match else 'N/A',
        'phone': phone_match.group() if phone_match else 'N/A',
        'experience': experience_text,
        'education': education_text,
        'skills': extract_skills(skills_text) if skills_text != "N/A" else ['None']
    }
    print("Parsed Skills:", resume_data['skills'])

    return resume_data