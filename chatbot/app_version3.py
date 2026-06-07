cat > chatbot/app_version3.py <<'EOF'
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "what foods help recovery",
    "should i drink electrolytes",
    "i feel dizzy after exercise"
]

embeddings = model.encode(sentences)

query = "food"

query_embedding = model.encode([query])

scores = cosine_similarity(
    query_embedding,
    embeddings
)[0]

for sentence, score in zip(sentences, scores):
    print(sentence, "->", round(score, 3))
EOF