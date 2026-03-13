import streamlit as st
from modules.chatbot import ask_ai


companies = [
    "Amazon",
    "Google",
    "Meta",
    "Apple",
    "Netflix"
]


def generate_company_question(company):

    prompt = f"""
    Generate a coding interview problem commonly asked at {company}.

    Include:
    - problem description
    - function signature
    - example input/output
    """

    return ask_ai(prompt)


def run_faang_trainer():

    st.header("🏢 FAANG Interview Trainer")

    company = st.selectbox(
        "Choose Company",
        companies
    )

    if st.button("Generate Question"):

        with st.spinner("Generating company-specific question..."):

            question = generate_company_question(company)

            st.markdown(question)
