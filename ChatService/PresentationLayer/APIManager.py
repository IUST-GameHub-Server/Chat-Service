from ..LogicLayer.ChatLogicHandler import ChatLogicHandler
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/connect_session')
def connect_session(string):
    return "Not Implemented"

@app.route('/send_message')
def send_message(message):
    return "Not Implemented"


@app.route('/recieve_message')
def recieve_message():
    return "Not Implemented"
