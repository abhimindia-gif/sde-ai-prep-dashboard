import streamlit as st
import pandas as pd

def show_progress():

    data = {

        "Topic":[
        "Python",
        "DSA",
        "OOP",
        "System Design"
        ],

        "Score":[
        70,
        50,
        80,
        40
        ]
    }

    df = pd.DataFrame(data)

    st.bar_chart(df.set_index("Topic"))
