# Ñîáğàòü äàííûå îá àááğåâèàòóğàõ, êîäàõ è ğàñôèğîâêàõ âàëşò
 
from bs4 import BeautifulSoup
from requests import get
from pprint import pprint
from pandas import DataFrame
 
def clean(tag_elem, ind):
    return str(tag_elem).split('>')[ind].split('<')[0]
 
def clean_tag_lst(tag_lst):
    return [clean(t, 2) if '<a href' in str(t) else clean(t, 1) for t in tag_lst ]
 
url = 'https://en.wikipedia.org/wiki/ISO_4217'
 
page = get(url).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', class_='wikitable')
 
curr_codes = clean_tag_lst(table.find_all('td')[0::5])
curr_numbers = clean_tag_lst(table.find_all('td')[1::5])
curr_titles = clean_tag_lst(table.find_all('td')[3::5])
 
curr_table = DataFrame({
    'àááğåâèàòóğà': curr_codes,
    'êîä': curr_numbers,
    'ğàñøèôğîâêà': curr_titles,
})
 
curr_table.to_csv('currency.csv', index=False)
