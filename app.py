import streamlit as st
from modules.chatbot import ask_ai
from modules.daily_test import generate_test
from modules.code_editor import code_practice
from modules.analytics import show_progress
from modules.leetcode_simulator import run_leetcode
from modules.daily_interview import run_daily_interview
from modules.ai_planner import run_planner
from modules.faang_trainer import run_faang_trainer
from modules.job_market import run_job_market
from modules.resume_analyzer import run_resume_analyzer

st.title("🚀 AI SDE Prep Dashboard")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "AI Planner",
        "FAANG Trainer",
        "Market Intelligence",
        "Resume Analyzer",
        "Daily Interview",
        "Daily Test",
        "Code Practice",
        "Interview Simulator",
        "AI Tutor",
        "Progress"
    ]
)







if menu == "Home":

    st.header("Welcome")

    st.write("Your personal AI coding preparation dashboard")


elif menu == "Daily Test":

    st.header("Daily Interview Test")

    questions = generate_test()

    for i,q in enumerate(questions):

        st.write(f"Question {i+1}")
        st.write(q)


elif menu == "Code Practice":

    code_practice()


elif menu == "AI Tutor":

    st.header("Ask AI Tutor")

    question = st.text_input("Ask coding question")

    if question:

        answer = ask_ai(question)

        st.write(answer)


elif menu == "Progress":

    show_progress()


elif menu == "Interview Simulator":

    run_leetcode()


elif menu == "Daily Interview":

    run_daily_interview()


elif menu == "AI Planner":

    run_planner()


elif menu == "FAANG Trainer":

    run_faang_trainer()


elif menu == "Market Intelligence":

    run_job_market()


elif menu == "Resume Analyzer":

    run_resume_analyzer()
