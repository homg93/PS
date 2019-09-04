from sys import stdin

def go(arr,k,i,cnt):
	if cnt == 6:
		for c in parr:
			print(c,end=' ')
		print()
		return
	if (k+1 <= i):
		return
	parr.append(arr[i])
	go(arr,k,i+1,cnt+1)
	parr.pop()
	go(arr,k,i+1,cnt)

while True:
	s = list(map(int, stdin.readline().split()))
	k = s[0]
	parr = []

	if k == 0:
		break
	go(s,k,1,0)
	print()