import streamlit as st
import requests

st.title("Resume to JD Matcher")

API_URL = "http://127.0.0.1:8000/match"

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

jd = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "docx"]
)

if st.button("Match"):
    if not resume or not jd:
        st.warning("Please upload both Resume and Job Description")
    else:
        with st.spinner("Matching resume with job description..."):
            files = {
                "resume": (resume.name, resume.getvalue()),
                "jd": (jd.name, jd.getvalue())
            }

            try:
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result = response.json()

                    st.success("Matching completed!")

                    st.metric(
                        "Match Score",
                        f"{result['match_score']} %"
                    )

                    st.subheader("Resume Skills")
                    st.write(result["resume_skills"])

                    st.subheader("JD Skills")
                    st.write(result["jd_skills"])

                    st.subheader("Matched Skills")
                    st.write(result["matched_skills"])

                else:
                    st.error("API Error")
                    st.text(response.text)

            except Exception as e:
                st.error("Failed to connect to backend")
                st.exception(e)
