from data.config import WEATHER_API_TOKEN
import requests
import emoji
import time
import json
from bs4 import BeautifulSoup


def geo(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_TOKEN}&mode=html'
    responce = requests.get(url)
    html = responce.text

    soup = BeautifulSoup(html, 'lxml')
    sity = soup.find('body').find('div', style='font-size: medium; font-weight: bold; margin-bottom: 0px;').text
    temperature = soup.find\
        ('body').find('div', style='display: block; clear: left; font-size: medium; font-weight: bold; padding: '
                                   '0pt 3pt;').text
    clouds = soup.find('body').find('div', style='display: block; clear: left; font-size: small;').text
    humidity_wind_pressure = soup.find('body').find_all('div', style='display: block; clear: left;'
                                                                     ' color: gray; font-size: x-small;')

    humidity, wind, pressure, _ = (item.text for item in humidity_wind_pressure)
    finish_text = f'Населенный пункт -> {sity}\n' \
                  f'\nТемпература -> {temperature}\n' \
                  f'\nОблачность -> {clouds[8:]}\n' \
                  f'\nВлажность -> {humidity[10:]}\n' \
                  f'\nВетер -> {wind[6:]}'
    return finish_text


def city(city_name):
    city_name = str(city_name).lower()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_TOKEN}&mode=html'
    responce = requests.get(url)
    html = responce.text

    soup = BeautifulSoup(html, 'lxml')
    sity = soup.find('body').find('div', style='font-size: medium; font-weight: bold; margin-bottom: 0px;').text
    temperature = soup.find\
        ('body').find('div', style='display: block; clear: left; font-size: medium; font-weight: bold; padding: '
                                   '0pt 3pt;').text
    clouds = soup.find('body').find('div', style='display: block; clear: left; font-size: small;').text
    humidity_wind_pressure = soup.find('body').find_all('div', style='display: block; clear: left;'
                                                                     ' color: gray; font-size: x-small;')

    humidity, wind, pressure, _ = (item.text for item in humidity_wind_pressure)
    finish_text = f'Населенный пункт -> {sity}\n' \
                  f'\nТемпература -> {temperature}\n' \
                  f'\nОблачность -> {clouds[8:]}\n' \
                  f'\nВлажность -> {humidity[10:]}\n' \
                  f'\nВетер -> {wind[6:]}'
    return finish_text


def new_weather(lat, lon, how_many_days):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={WEATHER_API_TOKEN}&units=metric'
    responce = requests.get(url)
    data = json.loads(responce.text)
    days_data = data['daily']
    day = days_data[how_many_days]
    # TODO Поправить . Ввод кол-ва дней
    # Текущая дата
    date = time.ctime(day['dt'])[:10]
    if date[:3] == 'Wed':
        date = 'Среда ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Thu':
        date = 'Черверг ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Fri':
        date = 'Пятница ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Sat':
        date = 'Суббота ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Sun':
        date = 'Воскресенье ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Mon':
        date = 'Понедельник ' + date[-2:] + ' ' + date[4:7]
    elif date[:3] == 'Tue':
        date = 'Вторник ' + date[-2:] + ' ' + date[4:7]
    # Время рассвета и заката
    sunrise = time.ctime(day['sunrise'])[11:19]
    sunset = time.ctime(day['sunset'])[11:19]
    # Мин и макс температура
    temperature_min = str(int(day['temp']['min'])) + '°C'
    temperature_max = str(int(day['temp']['max'])) + '°C'
    # Температура утром + ощущения
    temperature_morning = str(int(day['temp']['morn'])) + '°C'
    feels_like_morning = str(int(day['feels_like']['morn'])) + '°C'
    # Температура днем + ощущения
    temperature_day = str(int(day['temp']['day'])) + '°C'
    feels_like_day = str(int(day['feels_like']['day'])) + '°C'
    # Температура вечером + ощущения
    temperature_evening = str(int(day['temp']['eve'])) + '°C'
    feels_like_evening = str(int(day['feels_like']['eve'])) + '°C'
    # Температура ночью + ощущения
    temperature_night = str(int(day['temp']['night'])) + '°C'
    feels_like_night = str(int(day['feels_like']['night'])) + '°C'
    # Влажность
    humidity = str(day['humidity']) + '%'
    # Скорость ветра
    wind_speed = str(day['wind_speed'])
    # Направление ветра
    wind_deg = float(day['wind_deg'])
    if wind_deg > 326.25 or wind_deg < 11.25:
        wind_deg = 'северный ' + emoji.emojize(':arrow_up:', use_aliases=True)
    elif 56.25 > wind_deg > 11.25:
        wind_deg = 'северо-восточный ' + emoji.emojize(':arrow_upper_right:', use_aliases=True)
    elif 101.25 > wind_deg > 56.25:
        wind_deg = 'восточный ' + emoji.emojize(':arrow_right:', use_aliases=True)
    elif 146.25 > wind_deg > 101.25:
        wind_deg = 'юго-восточный ' + emoji.emojize(':arrow_lower_right:', use_aliases=True)
    elif 191.25 > wind_deg > 146.25:
        wind_deg = 'южный ' + emoji.emojize(':arrow_down:', use_aliases=True)
    elif 236.25 > wind_deg > 191.25:
        wind_deg = 'юго-западный ' + emoji.emojize(':arrow_lower_left:', use_aliases=True)
    elif 281.25 > wind_deg > 236.25:
        wind_deg = 'западный ' + emoji.emojize(':arrow_left:', use_aliases=True)
    elif 326.25 > wind_deg > 281.25:
        wind_deg = 'северо-западный ' + emoji.emojize(':arrow_upper_left:', use_aliases=True)

    # Облачность
    clouds = str(day['clouds']) + '%'
    # Погода(дождь, солнечно или облака)
    weather_main = day['weather'][0]['main']
    weather_description = day['weather'][0]['description']
    final_text = f'{date}\n' \
                 f'\n' \
                 f'Время рассвета: {sunrise}\n' \
                 f'Время заката:     {sunset}\n' \
                 f'\n' \
                 f'-------------------------------------------------------------\n' \
                 f'          Температура | Ощущается как \n' \
                 f'-------------------------------------------------------------\n' \
                 f'утром     {temperature_morning:^11}      {feels_like_morning:^13}\n' \
                 f'\n' \
                 f'днем      {temperature_day:^11}      {feels_like_day:^13}\n' \
                 f'\n' \
                 f'вечером  {temperature_evening:^11}      {feels_like_evening:^13}\n' \
                 f'\n' \
                 f'ночью      {temperature_night:^11}      {feels_like_night:^13}\n' \
                 f'-------------------------------------------------------------\n' \
                 f'Влажность воздуха: {humidity}\n' \
                 f'\n' \
                 f'Ветер: {wind_deg} {wind_speed}м/с\n' \
                 f'\n'

    return final_text