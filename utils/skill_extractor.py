def extract_skills(resume_text):

    skills_db = [
        "Python",
        "Java",
        "C",
        "SQL",
        "MySQL",
        "Machine Learning",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Streamlit",
        "HTML",
        "CSS",
        "GitHub"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return found_skills