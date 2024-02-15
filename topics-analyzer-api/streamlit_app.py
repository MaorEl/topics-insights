import streamlit as st
import core_handler
import json
import pandas as pd

st.title('topics insights app')

st.image('twitter-analytics.jpg')

with st.form("sign up"):
    st.header("sign up")
    user_id = st.text_input("user id:")
    input_topics = st.text_input("Enter the topics you want to start following (comma-separated):")
    submitted_sign_up = st.form_submit_button("Submit")

if submitted_sign_up:
    st.write("sign up result:", core_handler.core_sign_up(user_id, input_topics))


with st.form("analyze"):
    st.header("analyze")
    topic_to_analyze = st.text_input('enter a topic you want to analyze')
    submitted_analyze_result = st.form_submit_button("Submit")

if submitted_analyze_result:
    st.write('analyze result: ', core_handler.core_analyze(topic_to_analyze))


with st.form("visualize"):
    st.header("visualize")
    topic_to_visualize = st.text_input('enter a topic you want to visualize the analyzation')
    submitted_visualize_result = st.form_submit_button("Submit")

if submitted_visualize_result:
    df = pd.DataFrame(json.loads(core_handler.core_visualize(topic_to_visualize))["y"])
    st.write('The graph illustrates the correlation between the number of tweets (X-axis) and the corresponding level of excitement (Y-axis).')
    st.bar_chart(data=df)