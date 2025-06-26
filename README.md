# Sentiment Analysis Web App

A complete end-to-end sentiment analysis application built with Streamlit, trained on a multi-class dataset (positive, neutral, negative), and deployed using Docker.

## Features

* Clean UI for user input
* Text preprocessing and prediction
* Supports BERT and TF-IDF vectorizers
* Best model automatically selected using MLflow
* Containerized for easy deployment

## Quick Start

### Pull Docker Image

```bash
docker pull batman21/sentiment-app
```

### Run the App

```bash
docker run -p 8501:8501 batman21/sentiment-app
```

Then open your browser and go to: `http://localhost:8501`

---

## Model Experimentation

Throughout the development process, multiple models and vectorizers were experimented with:

### Vectorizers Used

* TF-IDF
* BERT Embeddings (sentence-transformers)

### Class Balancing Techniques

* SMOTE (Synthetic Minority Over-sampling Technique) was applied to address class imbalance in training data.

### Models Evaluated

* Logistic Regression
* SVM
* Random Forest
* XGBoost

### Best Model & Accuracy

* **Best Combination**: `BERT Embeddings + XGBoost`
* **Test Accuracy**: **78.35%**

The model and vectorizer were tracked using MLflow, and the best-performing model was automatically selected and exported.

---

## Tech Stack

* Python
* Streamlit
* XGBoost
* Sentence-Transformers
* SMOTE (imblearn)
* MLflow
* Docker

---

## Repository Structure

```bash
.
├── app.py                  # Streamlit interface
├── model.pkl               # Best trained XGBoost model
├── vectorizer.pkl          # BERT embedding vectorizer
├── Dockerfile              # Docker config
├── requirements.txt        # Dependencies
└── README.md
```

---

---

## Author

Adarsh

---

Feel free to raise issues or open PRs to contribute!
