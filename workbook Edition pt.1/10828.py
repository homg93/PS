import sys
arr = []
def push(k):
	arr.append(k)

def pop():
	global arr
	if empty():
		return -1
	else:
		temp = arr[-1]
		arr = arr[:-1]
		return temp

def size():
	return len(arr)
def empty():
	if len(arr) == 0:
		return 1
	else:
		return 0
def top():
	if len(arr) == 0:
		return -1
	else:
		return arr[-1]

n = int(sys.stdin.readline())
for _ in range(n):
	k = sys.stdin.readline().rstrip()
	if 'push' in k:
		_, num = k.split()
		push(num)
	elif k == 'top':
		print(top())
	elif k == 'pop':
		print(pop())
	elif k == 'size':
		print(size())
	elif k == 'empty':
		print(empty())



