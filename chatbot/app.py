#Version 1 Protoptype
import csv
import json

print("Heat Stress Assistant Chatbot")
print("--------------------------------")

# Load training examples
training_examples = {}

with open("../data/training_examples.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        question = row["question"].strip().lower()
        category = row["category"].strip()

        training_examples[question] = category

# Load response templates
with open("../data/response_templates.json", "r") as file:
    responses = json.load(file)

# Ask user question
user_question = input("\nAsk a question: ").strip().lower()

# Find matching category
if user_question in training_examples:

    category = training_examples[user_question]

    print("\nCategory:", category)
    print("\nResponse:")
    print(responses[category])

else:

    print("\nSorry, I do not understand that question yet.")
