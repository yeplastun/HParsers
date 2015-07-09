# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re


# encode: utf-8 -> bytes
# decode: bytes -> utf-8


def getGoogleLinks(query):
    url = "http://www.google.com/search?&q=" + query
    url = url.replace(' ', '+')
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, 'html.parser')
    soup = soup.body
    links = []
    for i in soup.findAll('h3', {'class': 'r'}):
        tag = i.find('a')
        links.append(tag['href'])
    pattern = re.compile('http.+&sa')
    results = map(lambda s: pattern.search(s).group()[:-3]
                  if pattern.search(s) else '', links)
    results = list(filter(lambda x: False if x == '' else True, results))
    return results
