from textblob import TextBlob

reviews = [
    "This product is amazing",
    "The quality is very bad",
    "The package arrived today"
]

for review in reviews:
    analysis = TextBlob(review)

    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"

    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    print("Review:", review)
    print("Sentiment:", sentiment)
    print()