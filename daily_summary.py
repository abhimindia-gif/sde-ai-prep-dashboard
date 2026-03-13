import schedule
import time
from modules.chatbot import ask_ai


def generate_summary():

    progress_data = """
    Example progress data
    problems solved: 5
    weak topic: graphs
    """

    prompt = f"""
    Create a daily interview prep summary for a student.

    Data:
    {progress_data}
    """

    summary = ask_ai(prompt)

    print(summary)


schedule.every().day.at("21:00").do(generate_summary)

while True:

    schedule.run_pending()
    time.sleep(60)
