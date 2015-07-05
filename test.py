import Google

l = [0,1,2,3,4,5,6,7,8,9]
l =list(filter(lambda x: 0 if x % 2 == 0 else 1, l))

for i in l:
	print(i)
