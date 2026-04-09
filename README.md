# 🚀 AI Resume Analyzer with ATS Score

## 📌 Overview

AI Resume Analyzer is a smart application that evaluates resumes against job descriptions and provides an ATS (Applicant Tracking System) score along with actionable feedback.

It combines rule-based NLP, machine learning (TF-IDF), and LLM-based analysis to simulate real-world resume screening used by recruiters.

---

## ✨ Features

* 📄 Resume parsing (PDF & DOCX support)
* 🧩 Section extraction (Skills, Experience, Education, Projects)
* 🔍 Skill extraction using dictionary + full-text analysis
* 📊 Job Description (JD) skill extraction
* 🤝 Skill matching (Resume vs JD)
* 📈 TF-IDF + Cosine Similarity for contextual matching
* 🎯 ATS score calculation (hybrid scoring system)
* 🧠 AI-powered feedback using LLM (Groq + LangChain)
* 🌐 Interactive UI with Streamlit

---

## 🧠 How It Works

1. Parse resume and extract structured sections
2. Extract skills from resume (section + full text)
3. Extract required skills from Job Description
4. Compare resume vs JD using:

   * Skill matching
   * TF-IDF similarity
5. Compute ATS score
6. Generate AI feedback for improvement

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn** (TF-IDF, Cosine Similarity)
* **LangChain + Groq (LLM)**
* **pdfplumber / python-docx**
* **Regex & NLP**

---

## 📂 Project Structure

```
Resume_Analyzer_Project/
│
├── app/
│   └── main.py              # Streamlit UI
│
├── core/
│   ├── parser.py           # Resume parsing
│   ├── extractor.py        # Skill extraction
│   ├── jd_parser.py        # JD processing
│   ├── matcher.py          # Similarity + ATS score
│   ├── feedback.py         # LLM feedback
│   └── pipeline.py         # End-to-end workflow
│
├── data/
│   └── skill.py            # Skill dictionary
│
├── test_parser.py          # Testing script
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
git clone  https://github.com/Krishna35-it/AI-Resume_Analyzer.git
cd AI-Resume-Analyzer
pip install -r requirements.txt
streamlit run app/main.py
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## 📊 Output

* ATS Score (%)
* Matched Skills
* Missing Skills
* AI-generated Feedback

---


## 🚀 Future Improvements

* Resume rewriting using LLM
* Advanced semantic matching (embeddings)
* Multi-job comparison
* Deployment (Streamlit Cloud / Hugging Face Spaces)

---

## 👤 Author

**Krishna Raj S**
