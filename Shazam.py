# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import requests
from Google import getGoogleLinks

# encode: utf-8 -> bytes
# decode: bytes -> utf-8


def getTrackTags(artist, track):
    term = ('site:www.shazam.com' + ' ' + artist + ' ' + track)
    links = getGoogleLinks(term)
    regex = 'http://www.shazam.com/track/[0-9]+/.+'
    pattern = re.compile(regex, re.IGNORECASE)
    links = list(filter(lambda x: 0 if pattern.match(x) == None else 1, links))
    regex = '\s*' + track + ' - ' + artist + '\s*'
    pattern = re.compile(regex, re.IGNORECASE)
    for link in links:
        soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        temp = soup.head.title.get_text()
        res = pattern.match(temp)
        if res is not None:
            soup = soup.find('p', {'class': 'trd-tag-count'})
            soup = soup.span
            counts = soup.string.replace(',', '')
            tags = int(counts)
            return tags
    return 'No data'
