import streamlit as st
import pdfplumber
from modules.chatbot import ask_ai


def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            text += page.extract_text()

    return text


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this software engineer resume.

    Identify:
    - strengths
    - missing skills
    - FAANG readiness
    - improvement suggestions

    Resume:
    {resume_text}
    """

    return ask_ai(prompt)


def run_resume_analyzer():

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)"
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        if st.button("Analyze Resume"):

            result = analyze_resume(text)

            st.markdown(result)
