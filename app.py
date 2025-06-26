import streamlit as st
import joblib
from sentence_transformers import SentenceTransformer
import numpy as np

# Load BERT embedder and XGBoost model
embedder = SentenceTransformer("all-MiniLM-L6-v2")
model = joblib.load("best_sentiment_model.pkl")  # model trained on 384-d BERT features

# Streamlit interface
user_input = st.text_area("Your Text", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        embedding = embedder.encode([user_input])
        prediction = model.predict(embedding)[0]

        sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
        st.success(f"**{sentiment_map[prediction]}**")
