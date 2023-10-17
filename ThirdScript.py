import json
import matplotlib.pyplot as plt
import numpy as np

def display_combined_plot():
    # Load tokenized comments from TokenizedByAI.json
    with open('TokenizedByAI.json', 'r', encoding='utf-8') as f:
        ai_comments = json.load(f)

    # Load tokenized comments from TokenizedComments.json
    with open('TokenizedComments.json', 'r', encoding='utf-8') as f:
        tokenized_data = json.load(f)
        tokenized_comments = tokenized_data["comments"]

    ai_positive_count = sum(1 for comment in ai_comments if comment["sentiment"] == "POSITIVE")
    ai_negative_count = sum(1 for comment in ai_comments if comment["sentiment"] == "NEGATIVE")

    tokenized_positive_count = sum(1 for comment in tokenized_comments if comment["sentiment"] == "Positive")
    tokenized_negative_count = sum(1 for comment in tokenized_comments if comment["sentiment"] == "Negative")

    ind = np.arange(4)
    width = 0.35

    data = [ai_positive_count, ai_negative_count, tokenized_positive_count, tokenized_negative_count]

    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size

    # Windows 10-like colors
    colors = ['#0078D7', '#FF4097', '#4CAF50', '#FF5252']

    rects1 = ax.bar(ind, data, width, color=colors, alpha=0.7)  # Adjust bar transparency

    ax.set_xlabel('Sentiment', fontsize=12, fontweight='bold', color='black')
    ax.set_ylabel('Number of Comments', fontsize=12, fontweight='bold', color='black')
    ax.set_title('Sentiment Analysis of Comments', fontsize=14, fontweight='bold', color='black')
    ax.set_xticks(ind)
    ax.set_xticklabels(('AI Positive', 'AI Negative', 'Tokenized Positive', 'Tokenized Negative'), fontsize=10, fontweight='bold', color='black')

    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

    ax.grid(True, linestyle='--', alpha=0.5, color='black')  # Add grid

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.show()

# Display combined plot
display_combined_plot()
