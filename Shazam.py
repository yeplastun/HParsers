# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
from Google import getGoogleLinks

# encode: utf-8 -> bytes
# decode: bytes -> utf-8

artist = 'Eminem'
track = 'Lose Yourself'

term = ('site:www.shazam.com'+' '+artist+' '+track)

links = getGoogleLinks(term)
for link in links:
	requests.get(link).text
