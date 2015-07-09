# -*- coding: utf-8 -*-

import re
from Google import getGoogleLinks
from requests import get
from bs4 import BeautifulSoup
# from urllib.parse import quote
# from mechanize import Browser


def getRotation(artist, track):
    query = 'site:www.moskva.fm' + ' ' + artist + ' ' + track
    links = getGoogleLinks(query)
    regex = 'http://www.moskva.fm/artist/.+/song_[0-9]+$'
    pattern = re.compile(regex, re.IGNORECASE)
    for link in links:
        if pattern.match(link) == None:
            continue
        regex = '[0-9]+$'
        sample = re.compile(regex)
        tmp = sample.search(link).group(0)
        link = 'http://www.moskva.fm/artist/' + artist.lower() + '/song_' + tmp
        soup = BeautifulSoup(get(link).text, 'html.parser')
        temp = soup.head.title.get_text()
        regex = '\s*"?\s*' + track + ' (-|—) ' + artist + ' (—|—) '
        sample = re.compile(regex, re.IGNORECASE)
        if sample.match(temp):
            soup = soup.body
            regex = '.+ротаци., послушали.+'
            sample = re.compile(regex, re.IGNORECASE)
            line = str(soup.find(text=sample))
            regex = '[0-9]+'
            sample = re.compile(regex, re.IGNORECASE)
            res = sample.search(line)
            if res is not None:
                rotation = int(res.group(0))
                return rotation
    return 'No data'
