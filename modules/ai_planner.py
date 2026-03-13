import streamlit as st
from modules.chatbot import ask_ai


def generate_plan(weeks, hours, external_course):

    prompt = f"""
    Create a FAANG software engineering interview preparation plan.

    Timeline: {weeks} weeks
    Study hours per day: {hours}

    External preparation resource:
    {external_course}

    Include:
    - weekly goals
    - daily study schedule
    - coding practice
    - system design
    """

    return ask_ai(prompt)


def run_planner():

    st.header("🧠 AI Study Planner")

    weeks = st.slider("Weeks until interviews",4,16,12)

    hours = st.slider("Daily study hours",1,6,2)

    external_course = st.text_area(
        "Third-party prep tool details"
    )

    if st.button("Generate Study Plan"):

        with st.spinner("Generating roadmap..."):

            plan = generate_plan(
                weeks,
                hours,
                external_course
            )

            st.markdown(plan)
