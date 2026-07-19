import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_resume_score
from utils.missing_skills import find_missing_skills
from utils.resume_suggestions import get_resume_suggestions
from utils.jd_matcher import calculate_jd_match

st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Resume Analyzer")

st.markdown("""
### Upload your resume and get AI-based analysis 🚀
""")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=150
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract Text
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    # Extract Skills
    skills = extract_skills(resume_text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.success(skill)

    # Resume Score
    score = calculate_resume_score(skills)

    st.subheader("Resume Score")

    st.progress(score)

    st.success(f"Your Resume Score: {score}/100")

    # Missing Skills
    missing_skills = find_missing_skills(skills)

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.warning(skill)

    # AI Suggestions
    suggestions = get_resume_suggestions(skills, score)

    st.subheader("AI Resume Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.info(suggestion)
    else:
        st.success("Excellent Resume! No major suggestions found.")

    # Job Description Match
    if job_description:

        jd_score = calculate_jd_match(
            skills,
            job_description
        )

        st.subheader("Job Description Match")

        st.progress(jd_score)

        st.success(f"Match Score: {jd_score}%")