# utils/sentiment_analysis.py

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_sentiment(text, model_path):
    with open("C:/Users/vasuv/OneDrive/Desktop/IIS_Deployment/models/lm_model.pkl", 'rb') as file:
        model = pickle.load(file)
        vectorizer = TfidfVectorizer()
        text = vectorizer.fit_transform(flpk_transformed.Review)
    # Perform sentiment analysis
    sentiment = model.predict([text])[0]
    return sentiment
