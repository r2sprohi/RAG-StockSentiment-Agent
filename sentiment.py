
import random

def analyze_sentiment(news_list):
    # Mock sentiment analysis for demo
    sentiments = ['Positive', 'Negative', 'Neutral']
    score = sum(random.choice([1, 0, -1]) for _ in news_list)
    if score > 0:
        return "UP 📈"
    elif score < 0:
        return "DOWN 📉"
    else:
        return "STAY ➖"
