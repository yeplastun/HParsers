# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import Google

# encode: utf-8 -> bytes
# decode: bytes -> utf-8

artist = 'Eminem'
track = 'Lose Yourself'

term = ('site:www.shazam.com'+' '+artist+' '+track).replace(' ','+')
