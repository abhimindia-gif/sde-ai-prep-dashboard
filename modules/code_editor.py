import streamlit as st
import traceback
from modules.chatbot import ask_ai

def code_practice():

    st.header("Python Practice Editor")

    code = st.text_area(
        "Write Python code",
        height=300
    )

    if st.button("Run Code"):

        try:

            exec(code)

            st.success("Code executed successfully")

        except Exception as e:

            error = traceback.format_exc()

            st.error(error)

            if st.button("Explain Error with AI"):

                explanation = ask_ai(
                    f"Explain this python error and how to fix it:\n{error}"
                )

                st.write(explanation)
