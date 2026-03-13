import streamlit as st
import requests
from bs4 import BeautifulSoup
from modules.chatbot import ask_ai


def scrape_jobs():

    url = "https://www.indeed.com/jobs?q=software+engineer&l=San+Jose"

    page = requests.get(url)

    soup = BeautifulSoup(page.text,"html.parser")

    jobs = soup.find_all("div")

    text_data = ""

    for job in jobs[:20]:

        text_data += job.get_text()

    return text_data


def analyze_market():

    data = scrape_jobs()

    prompt = f"""
    Analyze these job descriptions and extract the most demanded skills.

    Job data:
    {data}

    Output:
    - top programming languages
    - most demanded technologies
    - common interview topics
    """

    return ask_ai(prompt)


def run_job_market():

    st.header("📊 Job Market Intelligence")

    if st.button("Analyze Market"):

        with st.spinner("Scanning Bay Area job postings..."):

            result = analyze_market()

            st.markdown(result)
