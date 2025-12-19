# Resume-to-JD Matcher with Automated Screening & QnA Trigger

## Overview

This project automates the initial resume screening process by matching candidate resumes against job descriptions (JDs), computing a weighted match score, and applying a screening threshold to shortlist candidates. It then automatically triggers skill-based screening questions via email for shortlisted profiles, simulating a real-world Applicant Tracking System (ATS) workflow using NLP and machine learning.

---

## Objectives

- Parse resumes and job descriptions (PDF/DOCX)
- Extract and normalize technical skills
- Compute resume–JD match score
- Apply threshold-based screening logic
- Automatically trigger screening questions via email
- Provide a REST API and a simple UI for demonstration

---

## System Architecture

**Input**

- Candidate resume (PDF/DOCX)
- Job description (PDF/DOCX or text)

**Processing**

- Text parsing (PDF/DOCX)
- Skill extraction and normalization
- Semantic similarity (SBERT)
- Experience matching
- Weighted scoring
- Threshold decision

**Output**

- Match score (percentage)
- Shortlisting decision (SHORTLISTED/REJECTED)
- Screening email trigger status

---

## Technologies & Libraries

### Backend

- Python 3.12
- FastAPI
- pdfplumber (PDF parsing)
- python-docx (DOCX parsing)
- spaCy (NLP basics)
- scikit-learn (TF-IDF, cosine similarity)
- sentence-transformers (SBERT semantic similarity)
- smtplib (email automation)

### Frontend

- Streamlit (UI for upload & results)

---

## Scoring Rubric

| Component                       | Weight |
|---------------------------------|--------|
| Skill Overlap (Resume ∩ JD)     | 50%    |
| Semantic Similarity (SBERT)     | 30%    |
| Experience Matching             | 20%    |

**Final Score (%)** =  
\(0.50 \times \text{Skill Match}\)  
\(+ 0.30 \times \text{Semantic Similarity}\)  
\(+ 0.20 \times \text{Experience Match}\)

---

## Matching Components

### 1. Skill Extraction

- Regex-based word-boundary matching
- Normalized skill dictionary with synonyms
- Extracted independently from Resume and JD

### 2. Semantic Similarity

- SBERT embeddings (`all-MiniLM-L6-v2`)
- Captures contextual meaning beyond keywords

### 3. Experience Matching

- Regex-based extraction of years of experience
- Neutral scoring when JD does not specify experience (common for internships)

### 4. Threshold Logic

- Screening threshold set to **70%**
- If `score ≥ threshold` → Candidate is **SHORTLISTED**

---

## Automated Screening Trigger

When a candidate is shortlisted:

- Skill-based interview questions are generated
- Screening email is triggered via SMTP (simulated for demo)
- Email status is returned in the API response

> Email sending is logged/simulated to avoid exposing credentials. In production, credentials should be stored securely using environment variables.

---

## API Endpoints

### `POST /match`

Uploads a resume and JD, returns matching results.

**Response Example:**

{
"match_score": 80.33,
"threshold": 70,
"status": "SHORTLISTED",
"reason": "Score meets screening criteria",
"email_triggered": true,
"resume_skills": ["Python", "FastAPI", "NLP"],
"jd_skills": ["Python", "FastAPI", "Machine Learning"],
"matched_skills": ["Python", "FastAPI"]
}

<<<<<<< HEAD
text
=======


🖥️ UI Demo
>>>>>>> fe2c079 (Removed some unwanted files)

---

## UI Demo (Streamlit)

The Streamlit-based UI allows:

- File uploads for resume and JD
- Match score visualization
- Shortlist decision display
- Email trigger status display

---

## Project Structure

![WhatsApp Image 2025-12-17 at 11 09 00 PM](https://github.com/user-attachments/assets/a3c04c60-7254-4d4d-bd17-4770d5a16e4d)



---

## Evaluation Checklist

- Resume parsing: ✅  
- Skill & experience matching: ✅  
- Weighted scoring: ✅  
- Automated screening trigger: ✅  
- Clear explanation of match factors: ✅  

---

## Future Enhancements

- ATS webhook integration
- LLM-based dynamic question generation
- Role-specific weighting
- Multi-language resume support

---

## Author

**Shreyas T P**
