from flask import Flask, render_template, request, jsonify

from bot import chat

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("textbox.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chat(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)