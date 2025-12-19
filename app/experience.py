import re

def extract_years_of_experience(text: str) -> float:
    """
    Extract approximate total years of experience from text.
    Looks for patterns like:
    - 2 years
    - 1.5 years
    - 3+ years
    """
    text = text.lower()

    matches = re.findall(r"(\d+(\.\d+)?)\s*\+?\s*years?", text)

    years = [float(match[0]) for match in matches]

    if years:
        return max(years)  # take maximum mentioned
    return 0.0


def experience_match_score(
    resume_text: str,
    jd_text: str
) -> float:
    """
    Returns a score between 0 and 1
    """
    resume_years = extract_years_of_experience(resume_text)
    jd_years = extract_years_of_experience(jd_text)

    # If JD does not specify experience (common for interns)
    if jd_years == 0:
        return 0.7  # neutral score

    if resume_years >= jd_years:
        return 1.0

    return resume_years / jd_years
