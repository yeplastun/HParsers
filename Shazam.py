# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from Google import getGoogleLinks

# encode: utf-8 -> bytes
# decode: bytes -> utf-8

artist = 'Eminem'
track = 'Lose Yourself'
def getTrackTags(artist, track):
	term = ('site:www.shazam.com'+' '+artist+' '+track)
	links = getGoogleLinks(term)
	pattern = re.compile('http://www.shazam.com/track/[0-9]+/'+track.replace(' ','-')+'$',re.IGNORECASE)
	links = list(filter(lambda x: 0 if pattern.match(x) == None else 1, links))
	pattern = re.compile('\s+'+artist+'[\t\v\r\n\f]+',re.IGNORECASE)
	for link in links:
		soup = BeautifulSoup(requests.get(link).text,'html.parser')
		span = soup.body.find('span',{'itemprop' : 'name'})
		tempArtist = span.get_text()
		res = pattern.search(tempArtist)
		if res != None:
			soup = soup.find('p',{'class' : 'trd-tag-count'})
			soup = soup.span
			counts = soup.string.replace(',','')
			tags = int(counts)
			return counts
	return('No data')




