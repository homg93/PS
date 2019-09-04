import sys

def AC(p,n,arr):
	mybool = 1
	back = n
	front = 0
	result = ''

	for k in p:
		if k == 'R':
			mybool *= -1
		elif k == 'D':
			if front < back:
				if mybool == 1:
					front += 1
				elif mybool == -1:
					back -=1
	arr = arr[front:back]
	if mybool == -1:
		arr.reverse()
	result = '['+ ','.join(arr) + ']'
	return result

t = int(sys.stdin.readline())
for _ in range(t):
	isERR = 0
	p = sys.stdin.readline().rstrip()
	pcnt = p.count('D')
	n = int(sys.stdin.readline())
	arrs = sys.stdin.readline().rstrip()
	if pcnt == n:
		isERR = 2
	elif pcnt > n:
		isERR = 1
	elif arrs =='[]' and pcnt == 0:
		isERR = 2
	else:
		isERR = 0
		arr = arrs[1:-1].split(',')

	if isERR == 1:
		print('error')
	elif isERR == 2:
		print('[]')
	elif isERR == 0:
		print(AC(p,n,arr))