from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bot import chat

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chat(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)