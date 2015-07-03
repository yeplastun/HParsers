from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import urlopen

# -*- coding: utf-8 -*-

"""

using UTF-8 encoding for LFM API

Methods for LFM:

artist.getInfo
album.getInfo
track.getInfo

"""
#Account:
USER = "alla_cobra"
API_KEY = "f3bd5b0d18985e1b0d4bdc458879a39a"

def artistQuery(artist):
	data = {'method' : 'artist.getInfo','user' : USER,'api_key' : API_KEY,'artist' : artist}
	res = 'http://ws.audioscrobbler.com/2.0/?' + urlencode(data)
	return res

def trackQuery(artist, title):
	data = {'method' : 'track.getInfo','user' : USER,'api_key' : API_KEY,'artist' : artist,'track' : title}
	res = 'http://ws.audioscrobbler.com/2.0/?' + urlencode(data)
	return res

def getArtistScrobbles(artist):
	url = artistQuery(artist)
	res = urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	return soup.artist.playcount.get_text()

def getTrackScrobbles(artist,title):
	url = trackQuery(artist,title)
	res = urlopen(url)
	soup = BeautifulSoup(res,"html.parser")
	return soup.track.playcount.get_text()

url = artistQuery('Pink Floyd')
page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')
