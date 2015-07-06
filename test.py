import re
from Google import getGoogleLinks

artist = 'Eminem'
track = 'Lose Yourself'
temp = track + ' — ' + artist
s = 'Lose Yourself — Eminem — слушать бесплатно, текст песни — MOSKVA.FM'
regex = '\s*' + track + ' (—|—) ' + artist
pattern = re.compile(regex, re.IGNORECASE)
if pattern.match(s):
    print('yes')
q