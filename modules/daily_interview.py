import streamlit as st
import random
from modules.chatbot import ask_ai

topics = [
    "arrays",
    "hashmaps",
    "graphs",
    "trees",
    "dynamic programming"
]

difficulty_levels = [
    "easy",
    "medium",
    "medium",
    "hard"
]


def generate_interview_question():

    topic = random.choice(topics)
    difficulty = random.choice(difficulty_levels)

    prompt = f"""
    Generate a coding interview problem.

    Topic: {topic}
    Difficulty: {difficulty}

    Include:
    - problem description
    - function signature
    - example input/output
    """

    return ask_ai(prompt)


def run_daily_interview():

    st.header("🔥 Daily Interview Mode")

    if "questions" not in st.session_state:

        if st.button("Start Interview"):

            st.session_state.questions = []

            for i in range(4):

                q = generate_interview_question()

                st.session_state.questions.append(q)

    if "questions" in st.session_state:

        for i,q in enumerate(st.session_state.questions):

            st.markdown(f"### Question {i+1}")

            st.markdown(q)
