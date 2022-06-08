from flask import Flask, request, render_template, request, jsonify
# from flask_cors import CORS
from Chatbot_Application.Chatbot.bot import chat
from flask_apscheduler import APScheduler
from Chatbot_Application.Chatbot.autoScraper import views

app = Flask(__name__)
# scheduler = APScheduler()
# CORS(app)

@app.route('/')
def index():
    # print('Request for index page received')
    # return render_template('html/home.html')
    return "Hello, Flask!"

@app.route('/textbox.html')
def chatpage():
    # print('Request for textbox page received')
    # return render_template('html/textbox.html')
    return "Hello, Flask!"



# @app.post("/predict")
# def predict():
#     text = request.get_json().get("message")
#     response = chat(text)
#     message = {"answer": response}
#     return jsonify(message)



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