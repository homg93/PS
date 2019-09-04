import sys
q = []
def push(k):
	q.append(k)
def pop():
	global q
	if empty():return -1
	else:
		temp = q[0]
		q = q[1:]
		return temp
def size():
	return len(q)
def empty():
	if q:return 0
	else:return 1
def front():
	if empty():return -1
	else:return q[0]
def back():
	if empty():return -1
	else:return q[-1]

n = int(sys.stdin.readline())
for _ in range(n):
	k = sys.stdin.readline().rstrip()
	if k == 'front':print(front())
	elif k == 'back':print(back())
	elif k == 'pop':print(pop())
	elif k == 'size':print(size())
	elif k == 'empty':print(empty())
	else:_, num = k.split();push(num)