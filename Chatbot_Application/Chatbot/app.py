from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
# from flask_cors import CORS
from Chatbot_Application.Chatbot.bot import chat
from flask_apscheduler import APScheduler
from Chatbot_Application.Chatbot.autoScraper import views


app = Flask(__name__,
static_url_path='',
static_folder=os.path.abspath('Chatbot_Application/Chatbot/static')
)

# scheduler = APScheduler()
# CORS(app)

@app.route('/')
def home():
    print('Request for Home page received')
    return render_template('html/home.html')

@app.route('/textbox.html')
def chatpage():
    print('Request for textbox page received')
    return render_template('html/textbox.html')

@app.route('/index.html')
def index():
    print('request for index received')
    return render_template('html/index.html')



@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chat(text)
    message = {"answer": response}
    return jsonify(message)



# def scheduledTask():
#     views.update_games()

# def scheduledTask2():
#     views.update_players()

# def scheduledTask3():
#     views.update_medals()

if __name__ == '__main__':
    # runs task every hour
    # scheduler.add_job(id ='Scheduled task', func = scheduledTask, trigger = 'interval', seconds = 3600)
    # scheduler.add_job(id ='Scheduled task3', func = scheduledTask3, trigger = 'interval', seconds = 3600)
    # runs task every week
    # scheduler.add_job(id ='Scheduled task2', func = scheduledTask2, trigger = 'interval', seconds = 604800)
    # scheduler.start()
    app.run()