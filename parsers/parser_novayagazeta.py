
from ast import Not
import os
import sys
import requests
import datetime
import time

from bs4 import BeautifulSoup

sys.path.append('.')
from config import redis_db


URL = 'https://novayagazeta.ru/'

def parser_object():
    response = requests.get(f'{URL}feed/rss').text
    urls = BeautifulSoup(response, 'xml').find_all('link')
    return [url.getText() for url in urls]


def get_history(list_):
    print(list_)
    dict_urls = {}
    for url in list_:
        print(url)
        if redis_db.get(url) is None:
            print(redis_db.set(url, url))
            dict_urls[url] = url
    return dict_urls

def get_data_ng(dict_urls):
    return [url for _, url in dict_urls]
