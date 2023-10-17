import json
from transformers import pipeline

# Load pre-trained model for sentiment analysis
model = pipeline("sentiment-analysis")

# Load comments from the RawComments.json file
with open('RawComments.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    comments = data["comments"]

# Analyze sentiment for each comment
sentiments = model(comments)

# Tokenize comments and add sentiments
tokenized_comments = []
for comment, sentiment in zip(comments, sentiments):
    tokenized_comment = {
        "comment": comment,
        "sentiment": sentiment["label"],
        "tokens": []  # Placeholder, as we're not tokenizing here
    }
    tokenized_comments.append(tokenized_comment)

# Save data to JSON file
output_file = 'TokenizedByAI.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(tokenized_comments, f, ensure_ascii=False, indent=4)

print(f"Tokenized comments saved to {output_file}")
