# Resume-to-JD Matcher with Automated Screening & QnA Trigger

## 📌 Project Overview
This project automates the initial resume screening process by matching candidate resumes against job descriptions (JDs). It computes a weighted match score based on skills, semantic relevance, and experience, applies a screening threshold, and automatically triggers screening interview questions for shortlisted candidates.

The system simulates a real-world Applicant Tracking System (ATS) workflow using NLP and machine learning techniques.

---

## 🎯 Objectives
- Parse resumes and job descriptions (PDF/DOCX)
- Extract and normalize technical skills
- Compute resume–JD match score
- Apply threshold-based screening logic
- Automatically trigger screening questions via email
- Provide a REST API and a simple UI for demonstration

---

## 🧩 System Architecture
**Input** → Resume & JD  
**Processing** →
- Text Parsing
- Skill Extraction
- Semantic Similarity (SBERT)
- Experience Matching
- Weighted Scoring
- Threshold Decision  
**Output** →
- Match Score
- Shortlisting Decision
- Screening Email Trigger

---

## 🛠️ Technologies & Libraries Used

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

## ⚙️ Scoring Rubric (Core Logic)

| Component | Weight |
|---------|--------|
| Skill Overlap (Resume ∩ JD) | 50% |
| Semantic Similarity (SBERT) | 30% |
| Experience Matching | 20% |

**Final Score (%) =**
0.50 × Skill Match

0.30 × Semantic Similarity

0.20 × Experience Match


---

## 🧠 Matching Components Explained

### 1️⃣ Skill Extraction
- Regex-based word-boundary matching
- Normalized skill dictionary with synonyms
- Extracted independently from Resume & JD

### 2️⃣ Semantic Similarity
- SBERT embeddings (`all-MiniLM-L6-v2`)
- Captures contextual meaning beyond keywords

### 3️⃣ Experience Matching
- Regex-based extraction of years of experience
- Neutral scoring when JD does not specify experience (common for internships)

### 4️⃣ Threshold Logic
- Screening threshold set to **70%**
- If `score ≥ threshold` → Candidate shortlisted

---

## 📧 Automated Screening Trigger
When a candidate is shortlisted:
- Skill-based interview questions are generated
- Screening email is triggered via SMTP (simulated for demo)
- Email status is returned in API response

> Note: Email sending is logged/simulated to avoid exposing credentials. In production, credentials should be stored securely using environment variables.

---

## 🚀 API Endpoints

### `POST /match`
Uploads a resume and JD, returns matching results.

**Response Example:**
```json
{
  "match_score": 80.33,
  "threshold": 70,
  "status": "SHORTLISTED",
  "reason": "Score meets screening criteria",
  "email_triggered": true,
  "resume_skills": [...],
  "jd_skills": [...],
  "matched_skills": [...]
}

🖥️ UI Demo

A Streamlit-based UI allows:

File uploads

Match score visualization

Shortlist decision

Email trigger status display

Project Structure
resume-jd-matcher/
│── app/
│   ├── main.py
│   ├── parser.py
│   ├── skills.py
│   ├── matcher.py
│   ├── experience.py
│   ├── emailer.py
│── ui/
│   └── app.py
│── data/
│── tests/
│── README.md
│── requirements.txt

📊 Evaluation Criteria Satisfaction

Resume parsing: ✅
Skill & experience matching: ✅
Weighted scoring: ✅
Automated screening trigger: ✅
Clear explanation of match factors: ✅

🔮 Future Enhancements

ATS webhook integration
LLM-based dynamic question generation
Role-specific weighting
Multi-language resume support

👤 Author
Shreyas T P