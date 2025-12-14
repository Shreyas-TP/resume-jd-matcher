import re

SKILL_MAP = {
    # Programming Languages
    "Python": ["python", "py", "python3", "core python"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "C": ["c language"],
    "JavaScript": ["javascript", "js"],
    "SQL": ["sql", "mysql", "postgresql", "sqlite"],

    # Backend Frameworks
    "FastAPI": ["fastapi", "fast api"],
    "Flask": ["flask"],
    "Django": ["django"],
    "Spring Boot": ["spring boot"],

    # Data Science & ML
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning", "dl"],
    "NLP": ["nlp", "natural language processing"],
    "Computer Vision": ["computer vision", "cv"],
    "Data Science": ["data science"],

    # ML Libraries
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "TensorFlow": ["tensorflow", "tf"],
    "PyTorch": ["pytorch", "torch"],
    "Keras": ["keras"],

    # Data Handling & Visualization
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"],
    "Plotly": ["plotly"],

    # Databases
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo"],
    "SQLite": ["sqlite"],

    # Cloud & DevOps
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "GCP": ["gcp", "google cloud"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes", "k8s"],
    "CI/CD": ["ci/cd", "continuous integration"],

    # APIs & Web
    "REST API": ["rest api", "restful api"],
    "GraphQL": ["graphql"],
    "Microservices": ["microservices", "microservice"],

    # Version Control & Tools
    "Git": ["git", "github", "gitlab"],
    "Linux": ["linux", "ubuntu", "unix"],
    "Postman": ["postman"],

    # Testing
    "Unit Testing": ["unit testing"],
    "PyTest": ["pytest"],
    "Unittest": ["unittest"],

    # Other Useful Skills
    "OOP": ["oops", "object oriented programming"],
    "Data Structures": ["data structures", "dsa"],
    "Algorithms": ["algorithms"],
}


def extract_skills(text: str):
    """
    Extract and normalize skills from resume or JD text
    using word-boundary based matching to avoid false positives.
    """
    text = text.lower()
    found_skills = set()

    for skill, variants in SKILL_MAP.items():
        for variant in variants:
            pattern = rf"\b{re.escape(variant)}\b"
            if re.search(pattern, text):
                found_skills.add(skill)
                break  # stop checking other variants for this skill

    return list(found_skills)
