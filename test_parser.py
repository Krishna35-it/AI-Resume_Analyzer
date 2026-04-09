from core.parser import parse_resume
from core.extractor import extract_skills_from_sections, filtered_skills, extract_skills_from_resume
from core.jd_parser import read_jd_input, extract_skills_from_jd
from core.matcher import compute_tfidf_similarity,compute_ats_score
from core.feedback import generate_feedback
from langchain_groq import ChatGroq
import os




file_path = "data/Krishna_Raj_S_AI_ML_Trainee_Resume.pdf"

print("Current working directory:", os.getcwd())
print("Files in data folder:",os.listdir("data"))

print("Files exists:",os.path.exists(file_path))

result = parse_resume(file_path)

print("\n===== Raw Text =====")
print(result["raw_text"][:500])  # Print the first 500 characters of the raw text

print("\n===== Sections =====")
for section, content in result["sections"].items():
    print(f"\n--- {section.upper()} ---")
    print(content[:300])  # Print the first 300 characters of each section

print(result["sections"].keys())

skills_text = result["sections"].get("skills", "")

skills = extract_skills_from_sections(skills_text)
filtered_section_skill = filtered_skills(skills)

text_skills = extract_skills_from_resume(result["raw_text"])

#Combining skills from both sections and raw text
final_skills = list(set(filtered_section_skill + text_skills))

print("\n===== Final Extracted Skills =====")
print(final_skills)

jd_text = """Strong knowledge of Natural Language Processing (NLP)
Expertise in Machine Learning & Deep Learning models
Proficiency in Python programming
"""

jd_content = read_jd_input(jd_text)
jd_skills = extract_skills_from_jd(jd_content)

print("\n===== Extracted JD Skills =====")
print(jd_skills)

similarity_score = compute_tfidf_similarity(
    result["raw_text"],
    jd_text
)

print("\n===== TF-IDF Similarity Score =====")
print(round(similarity_score, 3))

ats_score, matched_skills = compute_ats_score(final_skills, jd_skills, similarity_score)

print("\n===== ATS Score =====")
print(f"ATS Score: {ats_score}%")   
print(f"Matched Skills: {matched_skills}")
print("\n===== MISSING SKILLS =====")
missing_skills = set(jd_skills) - set(final_skills)
print(list(missing_skills))

if not missing_skills:
    missing_skills = ["None"]


llm = ChatGroq(model = "llama-3.1-8b-instant",temperature = 0.3)

feedback = generate_feedback(
    llm,
    final_skills,
    jd_skills,
    missing_skills,
    ats_score
)

print("\n===== FEEDBACK =====") 
print(feedback)