from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_tfidf_similarity(resume_text, jd_text):
    """
    Compute the TF-IDF cosine similarity between the resume and job description.
    """
    vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,2),max_features=5000)
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def compute_ats_score(resume_skills,jd_skills,tfid_score):
    matched = set(resume_skills) & set(jd_skills)

    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = len(matched) / len(jd_skills)
    
    ats_score = (0.6 * skill_score) + (0.4 * tfid_score)

    return round(ats_score * 100, 2), matched