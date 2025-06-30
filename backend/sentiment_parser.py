\"\"\"
sentiment_parser.py – Extracts sentiment signals from user conversations using
simple rules or external libraries to classify emotional tone.
\"\"\"

from textblob import TextBlob

class SentimentParser:
    def analyze(self, text: str) -> str:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.2:
            return "positive"
        elif polarity < -0.2:
            return "negative"
        else:
            return "neutral"
