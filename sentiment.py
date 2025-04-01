from textblob import TextBlob

def analyze_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0.2:
        return "Positive", "😊"
    elif score < -0.2:
        return "Negative", "😟"
    else:
        return "Neutral", "😐"
