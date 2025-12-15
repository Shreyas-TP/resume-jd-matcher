from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    return cosine_similarity(
        [embeddings[0]], [embeddings[1]]
    )[0][0]


def skill_overlap_score(resume_skills, jd_skills):
    """
    Measures how many JD-required skills
    are present in resume skills
    """
    if not jd_skills:
        return 0.0

    matched = set(resume_skills).intersection(set(jd_skills))
    return len(matched) / len(jd_skills)


def final_match_score(
    resume_text,
    jd_text,
    resume_skills,
    jd_skills
):
    semantic = semantic_score(resume_text, jd_text)
    skill_overlap = skill_overlap_score(resume_skills, jd_skills)

    # INTERN-FRIENDLY WEIGHTS
    final_score = (
        0.55 * skill_overlap +
        0.30 * semantic +
        0.15 * min(1.0, semantic + skill_overlap)
    )

    return round(final_score * 100, 2)
