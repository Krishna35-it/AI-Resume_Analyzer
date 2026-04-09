from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

def generate_feedback(llm,resume_skills,jd_skills,missing_skills,ats_score):
    prompt = f"""
    You are an advanced ATS System and a career coach. A candidate has applied for a job and your task is to provide feedback on their resume based on the skills required for the job and the skills they have listed in their resume.

    Resume Skills: {resume_skills}
    Job Description Skills: {jd_skills}
    Missing Skills: {missing_skills}
    ATS Score: {ats_score}%

    IMPORTANT RULES:
    - ONLY use the provided data
    - DO NOT assume or add new skills
    - DO NOT hallucinate missing skills
    - DO NOT invent numbers or metrics
    - If no missing skills, explicitly say "No missing skills"


    Give Structured Feedback in the following format:
    1. Summary Match Analysis(2-3 lines)
    2. Missing Skills Explanation.(STRICTLY from missing_skills list)
    3. Specific Recommendations to improve the resume and increase the ATS score.(bullet points)(STRICTLY from missing_skills list)
    4. Rewrite one project description to better match the JD.
    """

    response = llm.invoke(prompt)

    return response.content