import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import tempfile
from langchain_groq import ChatGroq
from core.pipeline import analyze_resume

#Page Configuration
st.set_page_config(page_title="AI Resume Analyzer",layout = "wide")
st.title("AI Resume Analyzer and ATS Score Predictor")

#Input Section
uploaded_file = st.file_uploader("Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste the Job Description here")

#Iniatializing the LLM
llm = ChatGroq(model = "llama-3.1-8b-instant",temperature = 0.3)

#Analyze Button
if st.button("Analyze Resume"):

    if uploaded_file and jd_text:

        with st.spinner("Analyzing...."):
            #Saving the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name
            
            result = analyze_resume(tmp_file_path, jd_text, llm)

        #Displaying the results
        st.subheader("ATS Score")
        st.success(f"{result['ats_score']}%")

        st.subheader("Matched Skills")
        st.write(result["matched_skills"])

        st.subheader("Missing Skills")
        st.write(result["missing_skills"])

        st.subheader("LLM Feedback")
        st.write(result["feedback"])
    else:
        st.warning("Please upload a resume and paste the job description to analyze.")