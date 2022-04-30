"""
This code is used to run the trained chatbot
"""

# pip install tensorflow, nltk, numpy, scikit_learn, flask, flask-cors, Flask-APScheduler, selenium, webdriver-manager, tflearn
# python -m pip install Django

import json
import re 
import numpy as np

import pickle
from chatbot_backend.seleniumScraper import KeyValues, SQLMethods
import sqlite3
from sqlite3 import Error

import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import tflearn
import tensorflow as tf
import random

from datetime import datetime

data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

PersonsColumns =['Person ID','Contingent','Sport Name','Person Name', 'URL', 'Hometown', 'Type', 'Age', 'Height', 'Weight', 'Club', 'Coach', 'Position', 'Goals for Games', 'Personal Best Result', 'Award', 'Personal Role Model', 'Other Info']
with open('intents.json') as json_data:
    intents = json.load(json_data)


net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)


model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# load our saved model
model.load('./model.tflearn')


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1

    return(np.array(bag))



ERROR_THRESHOLD = 0.60
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def chat(sentence):
    results = classify(sentence)
    if results:
        while results:
            for i in intents['intents']:
                if i['tag'] == results[0][0]:
                    answer = random.choice(i['responses'])

                    # return the start date of Canada Summer Games
                    if answer == "TBD1":
                        return KeyValues.KeyValues.GameDay_Keys[0][0]


                    # returns information of a specific player 
                    elif answer == "TBD2":
                        temp = sentence.split(" ")
                        connection = SQLMethods.SQLMethods.create_connection(r"chatbot_backend/4P02 Chatbot Database.db")
                        max = len(temp)
                        ans = ""
                        res = []
                        url = None
                        for i in range(max):
                            if(i != max-1):
                                name = temp[i].capitalize() + " " + temp[i+1].capitalize()
                                res = SQLMethods.SQLMethods.sql_select_person_by_person_name_all_columns(connection, name)

                            if not res:
                                name = temp[i].capitalize()
                                res = SQLMethods.SQLMethods.sql_select_person_by_person_name_all_columns(connection, name)   
                            if res:
                                for r in res:
                                    count = len(r)
                                    for j in range(1,count):
                                        if (j == 4):
                                            url = r[j]
                                            continue
                                        if str(r[j]) != "None" and str(r[j]) != "NULL":
                                            ans = ans + "<strong>" + PersonsColumns[j] + ": </strong>" + str(r[j]) +"<br/>" 
                                    ans = ans + url + "<br/><br/>"
                                connection.close()
                                return ans
                        connection.close()
                        return "Could not find player, try full name." 


                    # returns the sport a specific player plays
                    elif answer == "TBD3":
                        temp = sentence.split(" ")
                        connection = SQLMethods.SQLMethods.create_connection(r"chatbot_backend/4P02 Chatbot Database.db")
                        max = len(temp)
                        ans = ""
                        res =[]
                        for i in range(max):
                            if (i != max-1):
                                name = temp[i].capitalize() + " " + temp[i+1].capitalize()
                                res = SQLMethods.SQLMethods.sql_select_person_by_person_name_sport_column_personName_column_contingent_column(connection, name)
                            
                            if(not res):
                                name = temp[i].capitalize()
                                res = SQLMethods.SQLMethods.sql_select_person_by_person_name_sport_column_personName_column_contingent_column(connection, name)

                            if res:
                                max2 = len(res)
                                ans = f"There are {str(max2)} player matching that name. <br/>"
                                for j in range(max2):
                                    if(max2 == 1):
                                        ans = "<i>" + res[j][0] + "</i>" + " " +  "participates in " + "<b>" + res[j][1] + "</b>"
                                    else:
                                        ans = ans + " <i>" + res[j][0] + "</i>" + " from " + "<i>" + res[j][2] + "</i>" + " participates in " + "<b>" + res[j][1] + "</b>.<br/>"
                                connection.close()
                                return ans 
                        connection.close()
                        return "Could not find player, try full name."


                    # returns how many medals a specific contingent has
                    elif answer == "TBD4":
                        temp = sentence.split(" ")
                        connection = SQLMethods.SQLMethods.create_connection(r"chatbot_backend/4P02 Chatbot Database.db")
                        max = len(KeyValues.KeyValues.Contingent_Keys)
                        temp2 = ""

                        for char in temp:
                            if char == "&":
                                char = "and"

                            if char != "and":                
                                temp2 = temp2 + char.capitalize() + " "
                            else: 
                                temp2 = temp2 + char + " "

                        for i in range(0,max):
                            if KeyValues.KeyValues.Contingent_Keys[i][0] in temp2:
                                res = SQLMethods.SQLMethods.sql_select_medals_from_contingents_by_contingentName(connection,KeyValues.KeyValues.Contingent_Keys[i][0])
                                if "silver" in sentence.lower():
                                    ans = res[0][0] + " currently has " + str(res[0][2]) + " silver medals"
                                    connection.close()
                                    return ans
                                elif "gold" in sentence.lower():
                                    ans = res[0][0] + " currently has " + str(res[0][1]) + " gold medals"
                                    connection.close()
                                    return ans
                                elif "bronze" in sentence.lower():
                                    ans = res[0][0] + " currently has "+ str(res[0][3]) + "</b>" + " bronze medals"
                                    connection.close()
                                    return ans
                                else:
                                    total = res[0][1] + res[0][2] + res[0][3]
                                    ans = res[0][0] + " currently has <b>"+ str(total) + "</b> medals. <b>" +str(res[0][1]) + "</b> gold, <b>" + str(res[0][2]) + "</b> silver, <b>" +str(res[0][3]) + "</b> bronze"
                                    connection.close()
                                    return ans
                        connection.close()
                        return "Cannot find province or territory by that name."


                    # returns the date for the next game of a contingent and/or a sport
                    elif answer == "TBD5":
                        temp = sentence.split(" ")
                        connection = SQLMethods.SQLMethods.create_connection(r"chatbot_backend/4P02 Chatbot Database.db")
                        max = len(KeyValues.KeyValues.Contingent_Keys)
                        max2 = len(KeyValues.KeyValues.Sport_Keys)
                        temp2 = ""
                        ans = ""
                        for char in temp:
                            if char == "&":
                                char = "and"

                            if char != "and":                
                                temp2 = temp2 + char.capitalize() + " "
                            else: 
                                temp2 = temp2 + char + " "
                        #no actual if so can be improved to speed up
                        # if user specifies a contingent with a game type
                        gameColumns = ['Game Name', 'Sport Name', 'Contingent' ,'Dates', 'Times', 'Location']
                        for i in range(0,max):
                            if KeyValues.KeyValues.Contingent_Keys[i][0] in temp2: 
                                for j in range(0,max2):
                                    if KeyValues.KeyValues.Sport_Keys[j][0] in temp2:
                                        res = SQLMethods.SQLMethods.sql_select_next_date_by_contingent_and_sport(connection, KeyValues.KeyValues.Contingent_Keys[i][0], 
                                            KeyValues.KeyValues.Sport_Keys[j][0])
                                        max3 = len(res)
                                        for k in range(0,max3):
                                            date_time = datetime.strptime(res[k][4], '%H:%M')
                                            ans = ans + "<b>" + gameColumns[0] + ": </b>" + res[k][0] + "</br><b>" + gameColumns[3] + ": </b>" + res[k][3] + "</br> <b>" + gameColumns[4] + ": </b>" + res[k][4] + "</br> <b>" + gameColumns[5] + ": </b>"+ res[k][5] + "<br> "
                                        connection.close()
                                        return ans


                        
                        #if users specifices contingent with no game type
                        for i in range(0,max):
                            if KeyValues.KeyValues.Contingent_Keys[i][0] in temp2:
                                res = SQLMethods.SQLMethods.sql_select_next_date_by_contingent(connection, KeyValues.KeyValues.Contingent_Keys[i][0])
                                max3 = len(res)
                                ans = "Here are the upcoming games for " + KeyValues.KeyValues.Contingent_Keys[i][0] + "<br>"
                                for k in range(0, max3):
                                    date_time = datetime.strptime(res[k][4], '%H:%M')
                                    ans = ans + "<b>" + gameColumns[0] + ": </b>" + res[k][0] + "</br> <b>"+ gameColumns[1] +": </b>" + res[k][1] + "</br><b>" + gameColumns[3] + ": </b>" + res[k][3] + "</br><b>" + gameColumns[4] + ": </b>" +res[k][4] + "</br> <b>" +gameColumns[5] + ": </b>"+ res[k][5] + "</br></br>"
                                connection.close()
                                return ans

                        
                        #if user specifices game type with no contingent 
                        for i in range(0,max2):
                            if KeyValues.KeyValues.Sport_Keys[i][0] in temp2:
                                res = SQLMethods.SQLMethods.sql_select_next_date_by_sportName(connection, KeyValues.KeyValues.Sport_Keys[i][0])
                                max3 = len(res)
                                for k in range(0,max3):
                                    date_time = datetime.strptime(res[k][4], '%H:%M')
                                    #print(date_time)
                                    ans = ans + "<b>" + gameColumns[0] + ": </b>" + res[k][0] + "</br> <b>" + gameColumns[2] + ": </b>" + res[k][2] + "</br><b>" + gameColumns[3] + ": </b>" + res[k][3] + "</br><b>" +  gameColumns[4] + ": </b>" +res[k][4] + "</br> <b>" + gameColumns[5] + ": </b>"+ res[k][5] + "</br></br>"
                                connection.close()
                                return ans
                        
                        connection.close
                        return "I could not find any information on that. Try adding the province/territory name."
                    
                    elif answer == "TBD6":
                        connection = SQLMethods.SQLMethods.create_connection(r"chatbot_backend/4P02 Chatbot Database.db")
                        res = SQLMethods.SQLMethods.select_all_sports(connection)
                        length = len(res)
                        ans = ""
                        for sport in res:
                            ans += sport[0] + "<br/>"
                        connection.close()
                        return ans

                    else:
                        return answer

                    
            results.pop(0)
    else:
        return "I'm sorry, I don't understand. Can you be more specific or you can go to this website https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"
        

if __name__ == "__main__":

    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = sentenceut("You: ")
        if sentence == "quit":
            break

        resp = chat(sentence)
        print(resp)