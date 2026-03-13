import streamlit as st
import traceback
import json
import random
from modules.chatbot import ask_ai


topics = [
    "arrays",
    "hashmaps",
    "graphs",
    "trees",
    "dynamic programming"
]


def load_progress():

    with open("data/progress.json") as f:

        return json.load(f)


def save_progress(data):

    with open("data/progress.json","w") as f:

        json.dump(data,f)


def generate_problem(topic):

    prompt = f"""
    Generate a Python coding interview problem.

    Topic: {topic}

    Include:
    - problem description
    - function signature
    - example input/output
    """

    return ask_ai(prompt)


def run_tests(code):

    test_cases = [
        ([2,7,11,15],9,[0,1]),
        ([3,2,4],6,[1,2]),
        ([3,3],6,[0,1])
    ]

    exec(code, globals())

    passed = 0

    for nums,target,expected in test_cases:

        result = two_sum(nums,target)

        if result == expected:

            passed += 1

    return passed, len(test_cases)


def run_leetcode():

    st.header("🧠 Coding Interview Simulator")

    if "topic" not in st.session_state:

        st.session_state.topic = random.choice(topics)

    st.write("Topic:", st.session_state.topic)

    if st.button("Generate Problem"):

        with st.spinner("Generating problem..."):

            st.session_state.problem = generate_problem(
                st.session_state.topic
            )

    if "problem" in st.session_state:

        st.markdown(st.session_state.problem)

        code = st.text_area(
            "Write your Python function",
            height=250,
            value="""def two_sum(nums,target):

    pass
"""
        )

        if st.button("Run Test Cases"):

            try:

                passed,total = run_tests(code)

                st.write(f"Score: {passed}/{total}")

                if passed < total:

                    st.error("Some tests failed")

                    progress = load_progress()

                    topic = st.session_state.topic

                    progress[topic] = progress.get(topic,0) + 1

                    save_progress(progress)

                    st.warning(
                        "Practice recommended for this topic"
                    )

                    if st.button("Start Practice Mode"):

                        st.session_state.topic = topic

                        st.session_state.problem = generate_problem(topic)

                else:

                    st.success("All tests passed")

            except Exception:

                error = traceback.format_exc()

                st.error(error)

                if st.button("Explain Error with AI"):

                    explanation = ask_ai(
                        f"Explain this Python error:\n{error}"
                    )

                    st.write(explanation)
