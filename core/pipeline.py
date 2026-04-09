from core.parser import parse_resume
from core.extractor import (
    extract_skills_from_resume,
    filtered_skills,
    extract_skills_from_sections
)
from core.jd_parser import extract_skills_from_jd
from core.matcher import compute_tfidf_similarity, compute_ats_score
from core.feedback import generate_feedback

def analyze_resume(file_path, jd_text, llm):

    #Step 1: Parse the resume and extract skills
    result = parse_resume(file_path)

    skills_text = result["sections"].get("skills","")
    section_skills = extract_skills_from_sections(skills_text)
    filtered_sections_skills = filtered_skills(section_skills)  

    #Step 2: Extract skills from the resume
    text_skills = extract_skills_from_resume(result["raw_text"])

    #Combining the skills
    final_skills = list(set(filtered_sections_skills + text_skills))

    #Step 3: Extract skills from the job description    
    jd_skills = extract_skills_from_jd(jd_text)

    #Step 4: Compute similarity and ATS score
    similarity_score = compute_tfidf_similarity(
        result["raw_text"],
        jd_text
    )

    #Step 5: Compute ATS Score
    ats_score, matched_skills = compute_ats_score(final_skills, jd_skills, similarity_score)

    #Step 6: Missing skills
    missing_skills = list(set(jd_skills) - set(final_skills))

    #Step 7: LLM Feedback
    feedback = generate_feedback(
        llm,
        final_skills,
        jd_skills,
        missing_skills,
        ats_score
    )

    return {
        "ats_score": float(ats_score),
        "matched_skills" : list(matched_skills),
        "missing_skills": missing_skills,
        "resume_skills": final_skills,
        "jd_skills": jd_skills,
        "feedback": feedback
    }