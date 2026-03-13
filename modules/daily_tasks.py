import streamlit as st


tasks = [
"Solve 2 graph problems",
"Practice system design question",
"Review recursion concepts",
"Complete third-party prep module"
]


def run_daily_tasks():

    st.header("📋 Daily Task Trainer")

    if "task_state" not in st.session_state:

        st.session_state.task_state = {}

    for task in tasks:

        done = st.checkbox(task)

        st.session_state.task_state[task] = done

    st.subheader("Outstanding Tasks")

    for task,status in st.session_state.task_state.items():

        if not status:

            st.error(task)
