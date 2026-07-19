def find_missing_skills(found_skills):

    all_skills = [
        "Python",
        "Java",
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

    missing_skills = []

    for skill in all_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills