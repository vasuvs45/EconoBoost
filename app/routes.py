# app/routes.py
from flask import render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from app import app

models = {
    "Logistic Model": "models/lm_model.pkl",
    "Multinomial Naive Bayes": "models/mb_model.pkl",
    "Random Forest":"models/rf_model.pkl",
    "SVM Model":"models/svm_model.pkl",
    "XGB Model":"models/xgb_model.pkl",
}

vectorizer_path = "models/vectorizer.pkl"

def analyze_sentiment(text, model_path,vectorizer_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    with open(vectorizer_path, 'rb') as file:
        vectorizer = pickle.load(file)
    text_vectorized  = vectorizer.transform([text]).toarray()
    print("Shape of text_vectorized:", text_vectorized.shape)
    sentiment = model.predict(text_vectorized)
    return sentiment[0]

@app.route('/')
def index():
    return render_template('index.html', models=models.keys())

@app.route('/analyze', methods=['POST'])
def analyze():    
    model_name = request.form['model']
    user_input = request.form['user_input']

    model_path = models[model_name]

    sentiment_int = analyze_sentiment(user_input, model_path,vectorizer_path)

    if sentiment_int == 0:
        sentiment = "😢"
    elif sentiment_int == 1:
        sentiment = "😐"
    else:
        sentiment = "😄"
    return render_template('result.html', sentiment=sentiment, user_input=user_input)
