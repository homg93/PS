import sys

t = int(sys.stdin.readline())
for _ in range(t):
	n,p = map(int, sys.stdin.readline().split())
	arr = list(map(int, sys.stdin.readline().split()))

	i = 0
	cnt = 1
	index = arr.index(max(arr))
	data = arr[p]
	mymax = max(arr)
	while(1):
		if data == mymax and index == p:
			break
		if arr[index] == mymax:
			cnt += 1
			arr[index] = 0
			mymax = max(arr)

		index = (index+1) % len(arr)
	print(cnt)