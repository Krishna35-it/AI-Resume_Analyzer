from core.extractor import extract_skills_from_resume

def read_jd_input(jd_input):
    #Incase of file path
    try:
        with open("jd_input","r",encoding = "utf-8") as f:
            return f.read()
    except:
        return jd_input
    
def extract_skills_from_jd(jd_text):
    return extract_skills_from_resume(jd_text)