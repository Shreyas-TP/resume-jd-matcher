from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def tfidf_score(resume, jd):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, jd])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

def semantic_score(resume, jd):
    emb = model.encode([resume, jd])
    return cosine_similarity([emb[0]], [emb[1]])[0][0]

def final_score(resume, jd):
    return round(
        (0.6 * tfidf_score(resume, jd) +
         0.4 * semantic_score(resume, jd)) * 100, 2
    )
