import os, re
import requests
import operator
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/tag/life/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {'class':'quote'})
        
all_text = ""
for quote in quotes:
    quote_text = quote.find('span', {'class': 'text'}).text
    all_text += quote_text + " "

# list of characters surrounded by word boundaries in the all_text string
all_words = re.findall(r'\b\w+\b', all_text.lower())

all_words_set = set(all_words)

# make a dictionary for frequency of words
freq = {}
for word in all_words_set:
    freq[word] = all_words.count(word)

# sorting the dictionary by value, in reverse
rank = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
top_5 = rank[:5]

rank = 1
for word, frequency in top_5:
    print(rank, word, frequency)
    rank += 1