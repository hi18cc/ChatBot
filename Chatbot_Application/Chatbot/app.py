from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bot import chat
from flask_apscheduler import APScheduler
from autoScraper import views

app = Flask(__name__)
scheduler = APScheduler()
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chat(text)
    message = {"answer": response}
    return jsonify(message)

def scheduledTask():
    views.update_games()

def scheduledTask2():
    views.update_players()

if __name__ == '__main__':
    # runs task every hour
    scheduler.add_job(id ='Scheduled task', func = scheduledTask, trigger = 'interval', seconds = 3600)
    # runs task every week
    scheduler.add_job(id ='Scheduled task2', func = scheduledTask2, trigger = 'interval', seconds = 604800)
    scheduler.start()
    app.run()