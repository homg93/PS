
# a,b = map(int, sys.stdin.readline().strip().split())
# print(a)
# print(b)
import sys

def myplus(t):
	mysum = 0
	myint = (sys.stdin.readline())

	for i in range(t):
		mysum += int(myint[i])
	print(mysum)

if __name__ == '__main__':
	t = int(sys.stdin.readline())
	myplus(t)