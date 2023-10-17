import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import nltk

# Download the necessary NLTK data
# nltk.download('punkt')



# Function to classify sentiment and tokenize comments
def classify_sentiment_and_tokenize(comments):
    sia = SentimentIntensityAnalyzer()
    tokenized_comments = []

    for comment in comments:
        # Perform sentiment analysis
        sentiment_score = sia.polarity_scores(comment)
        sentiment = "Positive" if sentiment_score['compound'] >= 0 else "Negative"

        # Tokenize the comment
        tokens = nltk.word_tokenize(comment)

        # Store sentiment, comment, and tokens
        tokenized_comments.append({
            "comment": comment,
            "sentiment": sentiment,
            "tokens": tokens
        })

    return tokenized_comments




# Download VADER lexicon (needed for sentiment analysis)
# nltk.download('vader_lexicon')

# Function to classify sentiment and tokenize comments
def classify_sentiment_and_tokenize(comments):
    sia = SentimentIntensityAnalyzer()
    tokenized_comments = []

    for comment in comments:
        # Perform sentiment analysis
        sentiment_score = sia.polarity_scores(comment)
        sentiment = "Positive" if sentiment_score['compound'] >= 0 else "Negative"

        # Tokenize the comment
        tokens = nltk.word_tokenize(comment)

        # Store sentiment, comment, and tokens
        tokenized_comments.append({
            "comment": comment,
            "sentiment": sentiment,
            "tokens": tokens
        })

    return tokenized_comments

# Load comments from the RawComments.json file
with open('RawComments.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    comments = data["comments"]

# Classify sentiment and tokenize comments
tokenized_comments = classify_sentiment_and_tokenize(comments)

# Create a dictionary to store tokenized comments
tokenized_data = {"comments": tokenized_comments}

# Save tokenized data to JSON file
output_file = 'TokenizedComments.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(tokenized_data, f, ensure_ascii=False, indent=4)

print(f"Tokenized comments saved to {output_file}")
