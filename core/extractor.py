import re
from data.skill import SKILL_SET, SKILL_ALIASES, normalize_skill


def clean_skill(skill):
    skill = skill.strip().lower()

    skill = re.sub(r"[()\[\]]"," ",skill)

    skill = re.sub(r"[^a-zA-Z0-9\s]", "", skill)

    skill = re.sub(r"\s+", " ", skill)

    return skill.strip()



def extract_skills_from_sections(skills_text):
    if not skills_text:
        return []
    
    #Normalizing the text
    skills_text = skills_text.lower()

    #Replacing common delimiters with a comma
    delimiters = ['\n', ';', '|', ' and ',':']

    for sep in delimiters:
        skills_text = skills_text.replace(sep, ',')
    
    #Spliting into tokens
    tokens = skills_text.split(',')

    #Cleaning tokens
    skills = [clean_skill(token) for token in tokens if token.strip()]

    return skills

def filtered_skills(extracted_skills):
    filtered = []

    for skill in extracted_skills:
        skill = normalize_skill(skill)

        #Applying alias mapping
        skill = SKILL_ALIASES.get(skill, skill)

        if skill in SKILL_SET:
            filtered.append(skill)
    
    return list(set(filtered))


def extract_skills_from_resume(text):
    text = text.lower()

    found_skills = set()

    #Checking direct matches
    for skill in SKILL_SET:
        if skill in text:
            found_skills.add(skill)
    
    #Checking alias matches
    for alias,actual in SKILL_ALIASES.items():
        if alias in text:
            found_skills.add(actual)
    
    return list(found_skills)