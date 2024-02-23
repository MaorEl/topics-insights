import streamlit as st
from repo.api_repository import ApiRepository
import json
import pandas as pd

api_repository = ApiRepository()


st.title('Topics Insights App')

st.image('twitter-analytics.jpg')

with st.form("Sign Up"):
    st.header("Sign Up")
    user_id = st.text_input("user id:")
    input_topics = st.text_input("Enter the topics you want to start following (comma-separated):")
    submitted_sign_up = st.form_submit_button("Submit")

if submitted_sign_up:
    st.write("sign up result:", api_repository.sign_up(user_id, input_topics))


with st.form("Analyze"):
    st.header("Analyze")
    topic_to_analyze = st.text_input('enter a topic you want to analyze')
    submitted_analyze_result = st.form_submit_button("Submit")

if submitted_analyze_result:
    st.write('Analyze result: ', api_repository.analyze(topic_to_analyze))


with st.form("Visualize"):
    st.header("Visualize")
    topic_to_visualize = st.text_input('enter a topic you want to visualize the analyzation')
    submitted_visualize_result = st.form_submit_button("Submit")

if submitted_visualize_result:
    df = pd.DataFrame(json.loads(api_repository.visualize(topic_to_visualize))["y"])
    st.write('The graph illustrates the correlation between the number of tweets (X-axis) and the corresponding level of excitement (Y-axis).')
    st.bar_chart(data=df)

