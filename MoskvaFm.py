import re
from Google import getGoogleLinks
from requests import get
from bs4 import BeautifulSoup
# from mechanize import Browser

artist = 'Eminem'
track = 'Lose Yourself'


def getRotation(artist, track):
    query = 'site:www.moskva.fm' + ' ' + artist + ' ' + track
    links = getGoogleLinks(query)
    regex = 'http://www.moskva.fm/artist/' + artist + '/song_[0-9]+$'
    pattern = re.compile(regex, re.IGNORECASE)
    for link in links:
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
            # soup.find('span', {a})

getRotation(artist, track)