import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
q = deque(maxlen=n)
for i in range(1,n+1):
	q.append(i)

cnt = 1
end = 0
print('<',end='')
while end < n:
	if q[0] == 0:
		q.append(q[0])
	elif cnt != k:
		q.append(q[0])
		cnt += 1
	else:
		cnt = 1
		end += 1
		print(q[0], end='')
		q.append(0)
		if end != n:
			print(', ',end='')
print('>',end='')
