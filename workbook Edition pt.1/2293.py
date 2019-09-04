import sys

def coin(n,k):
	a =[]
	dp = [0 for i in range(n)]
	cnt = 0
	for _ in range(n):
		a.append(int(sys.stdin.readline()))
	for i in range(n):
		if k % a[i] == 0:
			cnt +=1
		# for j in range(i+1,n):
		# 	k - a[i]
		# 	(lambda x: x%a[j] == 0,a)
		tsum = a[i]
		j = i+1
		while(tsum <= k):
			if tsum ==k:
				cnt += 1
				break
			tsum += a[j]
	while i<n:
		while tsum

n,k = map(int, sys.stdin.readline().split())