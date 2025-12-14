SKILL_MAP = {
    "Python": ["python", "py"],
    "Machine Learning": ["ml", "machine learning"],
    "FastAPI": ["fastapi", "fast api"],
    "NLP": ["nlp", "natural language processing"]
}

def extract_skills(text):
    text = text.lower()
    found = []

    for skill, variants in SKILL_MAP.items():
        for v in variants:
            if v in text:
                found.append(skill)
                break
    return list(set(found))
