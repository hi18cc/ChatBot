"""
This code is used to run the trained chatbot
"""

# pip install tensorflow, nltk, numpy, scikit_learn

import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)

def chat(inp):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    found = np.any(result >= 0.75)

    if found:
        for i in data['intents']:
            if i['tag'] == tag:
                return np.random.choice(i['responses'])
    else:
        return "ChatBot: I'm sorry, I don't understand. Can you be more specific or you can go to this website https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"
        

if __name__ == "__main__":

    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = chat(sentence)
        print(resp)