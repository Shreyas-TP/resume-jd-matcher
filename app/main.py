from fastapi import FastAPI, UploadFile
import shutil
import os

from .parser import extract_text
from .skills import extract_skills
from .matcher import final_match_score

app = FastAPI()

# Screening threshold (percentage)
SCREENING_THRESHOLD = 70.0


@app.post("/match")
async def match(resume: UploadFile, jd: UploadFile):
    # Ensure directories exist
    os.makedirs("data/resumes", exist_ok=True)
    os.makedirs("data/jds", exist_ok=True)

    resume_path = f"data/resumes/{resume.filename}"
    jd_path = f"data/jds/{jd.filename}"

    # Save files
    with open(resume_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    with open(jd_path, "wb") as f:
        shutil.copyfileobj(jd.file, f)

    # Extract text
    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    # Compute score (ensure Python float)
    score = float(
        final_match_score(
            resume_text,
            jd_text,
            resume_skills,
            jd_skills
        )
    )

    # Threshold decision
    if score >= SCREENING_THRESHOLD:
        status = "SHORTLISTED"
        reason = "Score meets minimum screening criteria"
    else:
        status = "NOT_SHORTLISTED"
        reason = "Score below screening threshold"

    return {
        "match_score": score,
        "threshold": SCREENING_THRESHOLD,
        "status": status,
        "reason": reason,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": list(
            set(resume_skills).intersection(set(jd_skills))
        )
    }
