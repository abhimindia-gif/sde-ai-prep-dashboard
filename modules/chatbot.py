import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
api_key = st.secrets.get("OPENAI_API_KEY")

# Safety check
if not api_key:
    st.error("OpenAI API key not configured. Please add it in Streamlit Secrets.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


def ask_ai(prompt):
    """
    Send a prompt to OpenAI and return the response.
    Handles errors so the app does not crash.
    """

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful coding interview tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"⚠️ AI request failed: {str(e)}"
