import sys
n,m = map(int, sys.stdin.readline().split())
q = [i for i in range(1,n+1)]
pq = list(map(int, sys.stdin.readline().split()))

pcnt = 0
cnt = 0
mid = 0
while pcnt != m:
	mid = len(q)//2
	if q[0] == pq[pcnt]:
		pcnt += 1
		q.pop(0)
	elif q.index(pq[pcnt]) - mid > 0:
		q.insert(0,q.pop())
		cnt +=1
	else:
		q.append(q.pop(0))
		cnt +=1
print(cnt)