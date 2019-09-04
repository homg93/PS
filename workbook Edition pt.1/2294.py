import sys

n, k = list(map(int, sys.stdin.readline().split()))
a = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    a.append(temp)

dp = []

for i in range(n-1,-1,-1):
	temp_k =  k - a[i]

