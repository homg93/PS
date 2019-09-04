import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	mcal = n
	i = 2
	arr = []
	cnt = 1

	while(mcal != 1):
		if mcal%i == 0:
			mcal //=i
			arr.append(i)
		else:
			i += 1
	# print(arr)
	if len(arr) == 1:
		print('%d %d' % (arr[0],cnt))
	for k in range(1,len(arr)):
		if arr[k-1] == arr[k]:
			cnt += 1
			if k == len(arr)-1:
				print('%d %d' % (arr[k],cnt))
		else:
			print('%d %d' % (arr[k-1],cnt))
			cnt = 1
			if k == len(arr)-1:
				print('%d %d' % (arr[k],cnt))