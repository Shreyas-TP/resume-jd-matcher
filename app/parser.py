import pdfplumber
from docx import Document

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

def extract_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def extract_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])
