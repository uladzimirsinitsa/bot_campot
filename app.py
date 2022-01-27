
import os
import requests
import time

from flask import Flask
from flask import jsonify
from flask import request as flask_request
from dotenv import load_dotenv

from .parsers import parser_meduza as pm
from .parsers import parser_novayagazeta as ng

load_dotenv()


app = Flask(__name__)


TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
URL = f'https://api.telegram.org/bot{TOKEN_TELEGRAM}/'
METHOD_SEND_MESSAGE = 'sendMessage'
LIST_COMMANDS = [
    '/mdz   meduza.io\n',
    '/ng    novayagazeta.ru\n'
                 ]


def parsing_get_request(request) -> tuple:
    chat_id = request['message']['chat']['id']
    message = request['message']['text']
    return chat_id, message


def parsing_get_message(message: str, LIST_COMMANDS: list) -> list:
    if'/mdz' in message:
        return pm.get_data_meduza()
    elif '/ng' in message:
        return ng.get_data_ng()
    else:
        return LIST_COMMANDS



def send_message(chat_id: int, text: str = ' ') -> dict:
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(f'{URL}{METHOD_SEND_MESSAGE}', json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if flask_request.method != 'POST':
        return '<h1>I am a bot and I live here. Why did you come?</h1>'

    obj = flask_request.get_json()
    chat_id, message = parsing_get_request(obj)
    list_data = parsing_get_message(message, LIST_COMMANDS)
    while list_data:
        send_message(chat_id, list_data.pop())
        time.sleep(0)


    return jsonify(obj)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
