import re

pattern = re.compile('http://www.shazam.com/track/[0-9]+/'+'lose-yourself',re.IGNORECASE)
s = 'http://www.shazam.com/track/11177141/lose-yourself'
res = pattern.match(s)
print(res)