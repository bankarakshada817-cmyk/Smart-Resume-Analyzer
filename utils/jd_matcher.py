def calculate_jd_match(skills, job_description):

    matched_skills = 0

    for skill in skills:
        if skill.lower() in job_description.lower():
            matched_skills += 1

    if len(skills) == 0:
        return 0

    match_score = int((matched_skills / len(skills)) * 100)

    return match_score