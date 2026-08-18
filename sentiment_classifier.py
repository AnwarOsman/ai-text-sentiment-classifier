# AI Text Sentiment Classifier
# Beginner-friendly machine learning project

from textblob import TextBlob


def classify_sentiment(text):
    """
    Classify a piece of text as Positive, Negative, or Neutral.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Example texts
examples = [
    "I love this course!",
    "This project is very difficult.",
    "The course is okay."
]

print("AI Text Sentiment Classifier")
print("-" * 30)

for text in examples:
    result = classify_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {result}")
    print()
