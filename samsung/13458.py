# -*- coding: utf-8 -*-
import sys
# p: place, s:student, c:care
def supervisor(p,s,c):
	cnt = 0

	for i in range(p):
		cnt += 1
		s[i] -= c[0]
		if(s[i] < 0):
			s[i] = 0

		rest = s[i] % c[1]
		share = s[i] // c[1]
		if (rest):
			cnt += 1+share
		else:
			cnt += share 

	print(cnt)

if __name__ == '__main__':
	p = int(sys.stdin.readline())
	s = list(map(int, sys.stdin.readline().split()))
	c = list(map(int, sys.stdin.readline().split()))

	supervisor(p,s,c)
