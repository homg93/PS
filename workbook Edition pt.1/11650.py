import sys
a=[]
n = int(sys.stdin.readline())
for _ in range(n):
	x,y = map(int, sys.stdin.readline().split())
	a.append([x,y])
a = sorted(a)
for x,y in a:
	print('%d %d' % (x,y))