import sys

def mystr(a):
	mylen = len(a)
	for i in range(mylen):
		if( i % 10 == 0 and i != 0):
			print()
		print(a[i], end='')

if __name__ == '__main__':
	a = sys.stdin.readline()
	mystr(a)