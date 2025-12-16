import smtplib
from email.message import EmailMessage


def send_screening_email(
    to_email: str,
    candidate_name: str,
    matched_skills: list
):
    """
    Sends screening interview questions based on matched skills.
    """

    # ---- EMAIL CONFIG (USE TEST / DUMMY CREDENTIALS) ----
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    FROM_EMAIL = "shreyastp8800@gmail.com"     
    FROM_PASSWORD = "your_app_password"      # use app password

    # ---- QUESTION GENERATION (RULE BASED) ----
    questions = []

    if "Python" in matched_skills:
        questions.append(
            "1. Explain Python file handling and exception handling."
        )

    if "Data Structures" in matched_skills:
        questions.append(
            "2. Explain any one data structure and its real-world use case."
        )

    if "Machine Learning" in matched_skills:
        questions.append(
            "3. What is overfitting? How do you prevent it?"
        )

    if "SQL" in matched_skills:
        questions.append(
            "4. Write a SQL query to find the second highest salary."
        )

    if not questions:
        questions.append(
            "1. Explain a recent technical project you worked on."
        )

    # ---- EMAIL BODY ----
    body = f"""
Hello {candidate_name},

Congratulations! Based on our initial screening, your profile matches the job requirements.

Please answer the following screening questions:

""" + "\n".join(questions) + """

Kindly reply with your answers.

Best regards,
TYASuite Hiring Team
"""

    msg = EmailMessage()
    msg["Subject"] = "Screening Questions – Python Developer Intern"
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    # ---- SEND EMAIL ----
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Email sending failed:", e)
        return False
