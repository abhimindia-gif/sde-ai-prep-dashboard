import streamlit as st
import random

from modules.database import init_db
from modules.welcome import run_welcome
from modules.ai_planner import run_planner
from modules.daily_tasks import run_daily_tasks
from modules.faang_trainer import run_faang_trainer
from modules.job_market import run_job_market
from modules.resume_analyzer import run_resume_analyzer
from modules.leetcode_simulator import run_leetcode
from modules.chatbot import ask_ai


# Initialize database
init_db()


st.set_page_config(
    page_title="Nishchitha AI Interview Coach",
    page_icon="🚀",
    layout="wide"
)


# Sidebar
st.sidebar.title("🚀 Nishchitha's AI Coach")


menu = st.sidebar.selectbox(

    "Navigation",

    [
        "Welcome",
        "AI Planner",
        "Daily Tasks",
        "FAANG Trainer",
        "Market Intelligence",
        "Resume Analyzer",
        "Interview Simulator",
        "AI Tutor",
    ]
)


# Welcome Page

if menu == "Welcome":

    run_welcome()


# AI Planner

elif menu == "AI Planner":

    st.title("🧠 AI Study Planner")

    run_planner()


# Daily Tasks

elif menu == "Daily Tasks":

    st.title("📋 Daily Tasks")

    run_daily_tasks()


# FAANG Trainer

elif menu == "FAANG Trainer":

    st.title("🏢 FAANG Interview Trainer")

    run_faang_trainer()


# Job Market

elif menu == "Market Intelligence":

    st.title("📊 Bay Area Job Market Intelligence")

    run_job_market()


# Resume Analyzer

elif menu == "Resume Analyzer":

    st.title("📄 Resume Analyzer")

    run_resume_analyzer()


# Coding Simulator

elif menu == "Interview Simulator":

    st.title("💻 Coding Interview Simulator")

    run_leetcode()


# AI Tutor

elif menu == "AI Tutor":

    st.title("🤖 AI Interview Tutor")

    question = st.text_input("Ask any coding interview question")

    if question:

        answer = ask_ai(question)

        st.write(answer)


# Footer

st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ for Nishchitha")
