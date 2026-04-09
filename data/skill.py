SKILL_SET = {
    #Programming Languages
    'python', 'java', 'c++', 'javascript','sql',
    #Libraries and Frameworks
    'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'tensorflow', 'keras',
    #ML /DL Concepts
    'machine learning', 'deep learning', 'natural language processing', 'computer vision','rnn','cnn','lstm',
    #Tools
    'power bi', 'tableau', 'excel', 'git', 'docker', 'kubernetes','streamlit','flask','django','fastapi','aws','azure',
    #Concepts
    'regression', 'classification', 'clustering', 'dimensionality reduction', 'feature engineering','data visualization','model evaluation','cross-validation','hyperparameter tuning'
}

SKILL_ALIASES = {
    'ml' : 'machine learning',
    'dl' : 'deep learning',
    'nlp' : 'natural language processing',
    'scikit learn' : 'scikit-learn',
    'powerbi' : 'power bi',
    'tf'  : 'tensorflow',
}

def normalize_skill(skill):
    """
    Normalize the skill by converting it to lowercase and stripping whitespace.
    """
    return skill.strip().lower()
