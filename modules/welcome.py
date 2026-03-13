import streamlit as st
import random
from modules.database import get_tasks, add_task, update_task


quotes = [
"Every problem you solve is one step closer to Google.",
"Consistency beats intensity.",
"You are building your future one algorithm at a time.",
"Small progress today = big success tomorrow."
]


def run_welcome():

    st.title("🌟 Welcome Nishchitha")

    st.subheader("How are you feeling today?")

    mood = st.text_input("Tell me about your day")

    if mood:

        st.success("Thanks for sharing! Let's make today productive 💪")


    st.subheader("📋 Today's Tasks")


    tasks = get_tasks()

    completed_count = 0


    for task_id, task, completed in tasks:

        checked = st.checkbox(task, value=bool(completed))

        update_task(task_id, int(checked))

        if checked:
            completed_count += 1


    if tasks:

        progress = completed_count / len(tasks)

        st.progress(progress)


    st.subheader("➕ Add New Task")

    new_task = st.text_input("Add task for today")

    if st.button("Add Task"):

        if new_task:

            add_task(new_task)

            st.success("Task added!")


    st.subheader("💡 Motivation")

    st.info(random.choice(quotes))
