import sys

def date(e,s,m):
	i = 0
	xe =xs =xm = 0
	
	while True:
		i +=1
		xe +=1
		xs +=1
		xm +=1
		if(xe == 16):
			xe = 1
		if(xs == 29):
			xs = 1
		if(xm == 20):
			xm = 1
		if (e == xe) and (s == xs) and (m == xm):
			print(i)
			break
if __name__ == '__main__':
	e,s,m = map(int, sys.stdin.readline().split())
	date(e,s,m)
