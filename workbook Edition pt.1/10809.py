import sys

def score(n):
	alpha = [-1]*26

	for i in range(len(n)-2,-1,-1):
		alpha[int(ord(n[i]))-97 ] = i
	
	for i in range(len(alpha)):
		if(i != 0):
			print(' ',end='')
		print(alpha[i],end='')

if __name__ == '__main__':
	n = sys.stdin.readline()
	score(n)

# for i in range(97,123):
# 	print(' ',end='') 
# 	print(chr(i), end ='')