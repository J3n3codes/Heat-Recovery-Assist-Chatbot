cat > chatbot/web_app.py <<'EOF'
import csv
import json
import numpy as np
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Heat Stress Assistant Chatbot")

questions = []
categories = []

with open("data/training_examples.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        questions.append(row["question"].strip().lower())
        categories.append(row["category"].strip())

with open("data/response_templates.json", "r") as file:
    responses = json.load(file)

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

user_question = st.text_input("Ask a question")

if user_question:
    user_vector = vectorizer.transform([user_question.lower()])
    similarities = cosine_similarity(user_vector, question_vectors)[0]

    best_match_index = np.argmax(similarities)
    best_score = similarities[best_match_index]

    best_question = questions[best_match_index]
    category = categories[best_match_index]

    if best_score >= 0.10:
        st.write("**Closest training question:**", best_question)
        st.write("**Similarity score:**", round(best_score, 3))
        st.write("**Category:**", category)
        st.success(responses[category])
    else:
        st.error("Sorry, I do not understand that question yet.")
EOF