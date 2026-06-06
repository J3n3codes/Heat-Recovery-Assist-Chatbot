import streamlit as st

st.title("Heat Stress Assistant Chatbot")

user_question = st.text_input("Ask a question")

if user_question:
    st.write("You asked:", user_question)
