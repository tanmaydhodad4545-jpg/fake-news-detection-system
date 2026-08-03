from flask import Flask, render_template, request

from predict import predict_news

from database.database import (
    create_table,
    save_prediction,
    get_predictions
)


app = Flask(__name__)


# Create database table
create_table()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def prediction():

    news_text = request.form["news"]

    result = predict_news(news_text)

    save_prediction(news_text, result)

    return render_template(
        "result.html",
        prediction=result,
        news=news_text
    )


# History page
@app.route("/history")
def history():

    data = get_predictions()

    return render_template(
        "history.html",
        predictions=data
    )


if __name__ == "__main__":
    app.run(debug=True)