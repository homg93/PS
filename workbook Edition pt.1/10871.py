import sys

def mylittle(n,x):
	mylist = list(map(int,sys.stdin.readline().split()))
	space = 0

	for i in range(n):
		if(mylist[i] < x):
			if(space == 0):
				space += 1
			else:
				print(' ',end='')
			print(mylist[i], end='')

if __name__ == '__main__':
	n,x = map(int,sys.stdin.readline().split())
	mylittle(n,x)