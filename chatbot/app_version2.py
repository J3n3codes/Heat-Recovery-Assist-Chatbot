# Version 2 Prototype
# TF-IDF + Cosine Similarity Chatbot

import csv
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Heat Stress Assistant Chatbot - Version 2")
print("------------------------------------------")

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

user_question = input("\nAsk a question: ").strip().lower()

user_vector = vectorizer.transform([user_question])
similarities = cosine_similarity(user_vector, question_vectors)[0]

best_match_index = np.argmax(similarities)
best_score = similarities[best_match_index]

best_question = questions[best_match_index]
category = categories[best_match_index]

if best_score >= 0.10:
    print("\nClosest training question:", best_question)
    print("Similarity score:", round(best_score, 3))
    print("Category:", category)

    print("\nResponse:")
    print(responses[category])
else:
    print("\nSorry, I do not understand that question yet.")