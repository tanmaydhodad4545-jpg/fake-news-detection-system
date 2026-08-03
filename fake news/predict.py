import joblib
from preprocessing import preprocess_text


# Load trained model and vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_news(news_text):

    # Clean text
    cleaned_text = preprocess_text(news_text)

    # Convert text to vector
    vector = vectorizer.transform([cleaned_text])

    # Prediction
    result = model.predict(vector)[0]

    if result == 0:
        return "Fake News"
    else:
        return "Real News"


# Test prediction
if __name__ == "__main__":

    news = input("Enter news text: ")

    prediction = predict_news(news)

    print("Prediction:", prediction)