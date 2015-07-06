import re
from Google import getGoogleLinks
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import quote
# from mechanize import Browser


def getRotation(artist, track):
    query = 'site:www.moskva.fm' + ' ' + artist + ' ' + track
    links = getGoogleLinks(query)
    regex = 'http://www.moskva.fm/artist/' + quote(artist) + '/song_[0-9]+$'
    pattern = re.compile(regex, re.IGNORECASE)
    for link in links:
        print(link)
        if pattern.match(link) == None:
            continue
        soup = BeautifulSoup(get(link).text, 'html.parser')
        # f = open('page.html', 'w')
        # f.write(soup.prettify())
        tempTrack = soup.head.title.get_text()
        regex = '\s*' + track + '\W+' + artist
        sample = re.compile(regex, re.IGNORECASE)
        if sample.match(tempTrack):
            soup = soup.body
            regex = '.+ротаций.+'
            sample = re.compile(regex, re.IGNORECASE)
            line = str(soup.find(text=sample))
            regex = '[0-9]+'
            sample = re.compile(regex, re.IGNORECASE)
            res = sample.search(line)
            rotation = int(res.group(0))
            return rotation
        return 'No data'


artist = 'Анжелика Агурбаш'
track = 'Я Не Вижу Солнца За Ночью'
print(getRotation(artist, track))
