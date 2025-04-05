
import streamlit as st
from sentiment import analyze_sentiment

st.title("RAG Stock Sentiment Agent")

user_news = []
for i in range(5):
    user_news.append(st.text_area(f"News Article {i+1}"))

if st.button("Predict Stock Movement"):
    prediction = analyze_sentiment(user_news)
    st.write(f"### Predicted Stock Movement: {prediction}")
