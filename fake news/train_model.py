import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from preprocessing import preprocess_text


# Load datasets
fake = pd.read_csv("dataset/Fake.csv")
real = pd.read_csv("dataset/True.csv")


# Add labels
fake["label"] = 0
real["label"] = 1


# Combine datasets
data = pd.concat([fake, real], axis=0)


# Shuffle data
data = data.sample(frac=1).reset_index(drop=True)


# Use news text
data["content"] = data["title"] + " " + data["text"]


# Apply preprocessing
data["content"] = data["content"].apply(preprocess_text)


# Features and labels
X = data["content"]
y = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# Train model
model = LogisticRegression()

model.fit(X_train, y_train)


# Test accuracy
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)


# Save model
joblib.dump(
    model,
    "models/fake_news_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)


print("Model saved successfully!")