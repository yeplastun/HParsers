import re

regex = '[а-я]+'
s = 'фывsdфывфыв'
pattern = re.compile(regex)
for p in pattern.search(s).span():
	print(p)