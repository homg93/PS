from sys import stdin

def go(k, tot):
	if k == tot:
		return 1
	if k < tot:
		return 0
	now = 0 #어떻게 돌아가고 값을 저장하는지
	for i in range(1,4):
		now += go(k,tot+i)
	return now

n = int(stdin.readline())
for i in range(n):
	k = int(stdin.readline())
	print(go(k,0))
