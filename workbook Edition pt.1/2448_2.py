import math

s = ['  *   ',' * *  ','***** ']

def star11(shift):
	c = len(s)
	for i in range(c):
		s.append(s[i]+s[i])
		print(s)
		s[i] = ("   " * shift + s[i]+ "   " * shift)
		print(s)
n= int(input())
k = int(math.log(n//3,2))

for i in range(k):
	star11(int(pow(2,i)))
for i in range(n):
	print(s[i])
