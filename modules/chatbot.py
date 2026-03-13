from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_ai(question):

    try:

        prompt = f"""
        You are a senior software engineer mentor helping someone prepare for coding interviews.

        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI error occurred: {str(e)}"
