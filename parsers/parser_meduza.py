"""Code for parsing meduza.io. """

import requests
import datetime

from bs4 import BeautifulSoup


URL_MEDUZA = 'https://meduza.io'


def format_todays_date():
    date = datetime.datetime.now()
    month = f'0{date.month}' if len(str(date.month)) < 2 else date.month
    day = f'0{date.day}' if len(str(date.day)) < 2 else date.day
    return f'/news/{date.year}/{month}/{day}/'


def parser_meduza(todays_date) -> list:
    links_news = []
    response = requests.get(URL_MEDUZA).text
    soup = BeautifulSoup(response, 'lxml').find_all('a')

    for obj in soup:
        obj = obj.get('href')
        if todays_date in obj:
            obj = f'{URL_MEDUZA}{obj}'
            links_news.extend(obj)
    return links_news[:2]


def get_data_meduza():
    todays_date = format_todays_date()
    return parser_meduza(todays_date)


if __name__ == "__main__":
    get_data_meduza()
