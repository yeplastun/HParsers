# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

# encode: utf-8 -> bytes
# decode: bytes -> utf-8

def getGoogleLinks(query):
	url = "http://www.google.com/search?&q="+query
	r = requests.get(url)
	doc = r.text
	soup = BeautifulSoup(doc,'html.parser') # получили html документ поисковой выдачи
	soup = soup.body
	links = []
	for i in soup.findAll('h3',{'class' : 'r'}):
		tag = i.find('a')
		links.append(tag['href'])
	pattern = re.compile('http.+&sa')
	results = map(lambda s: pattern.search(s).group()[:-3] if pattern.search(s) else "Wrong url",links)
	results = list(filter(lambda x: False if x == "Wrong url" else True, results))
	return results