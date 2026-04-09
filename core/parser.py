import pdfplumber
from docx import Document
import re

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_resume_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

def extract_sections(text):
    section_titles = [
        "summary","professional summary",
        "skills","technical skills", "skill"
        "experience","work experience","professional experience",
        "education","projects","project experience"
    ]

    pattern = r"(?im)^(%s)\s*$" % "|".join(section_titles)

    splits = re.split(pattern, text)

    section_map = {
        "summary": "summary",
        "professional summary": "summary",
        "skills": "skills",
        "technical skills": "skills",
        "skill": "skills",
        "experience": "experience",
        "work experience": "experience",
        "professional experience": "experience",
        "education": "education",
        "projects": "projects",
        "project experience": "projects"
    }

    sections = {}

    for i in range(1, len(splits), 2):
        raw_section = splits[i].strip().lower()
        section_name = section_map.get(raw_section, raw_section)
        section_content = splits[i + 1].strip()

        if section_name in sections:
            sections[section_name] += "\n" + section_content
        else:
            sections[section_name] = section_content

    return sections

def parse_resume(file_path):
    text = extract_resume_text(file_path)
    sections = extract_sections(text)
    return {
        "raw_text": text,
        "sections": sections
    }


