import requests
from random import choices
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(requests.get('https://mimuw.edu.pl').text, features='html.parser')

calendar_div = soup.find(class_='view-calendar')
lis = calendar_div.find_all('li')

events = []

for li in lis:
    title_par = li.find(class_='title')
    title = title_par.find('a').text
    href = 'https://mimuw.edu.pl' + title_par.find('a').get('href')
    date = li.find(class_='date').text


    print(title)
    print(href)
    print(date)

    events.append({
        'title': title,
        'href': href,
        'date': date,
    })


for e in choices(events, k=5):
    print(e)

df = pd.DataFrame(events)
df.to_csv('mimevents.csv')
    

    
