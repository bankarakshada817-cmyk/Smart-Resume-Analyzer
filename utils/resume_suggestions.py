def get_resume_suggestions(skills, score):

    suggestions = []

    if "HTML" not in skills:
        suggestions.append("Learn HTML for web development.")

    if "CSS" not in skills:
        suggestions.append("Learn CSS for better frontend skills.")

    if "GitHub" not in skills:
        suggestions.append("Add GitHub profile/projects.")

    if score < 60:
        suggestions.append("Add more projects and certifications.")

    return suggestions