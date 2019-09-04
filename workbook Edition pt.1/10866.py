import sys
q = []
def push_back(k):
	q.append(k)
def push_front(k):
	q.insert(0,k)
def pop_back():
	global q
	if empty():return -1
	else:
		return q.pop()
def pop_front():
	global q
	if empty():return -1
	else:
		return q.pop(0)
	
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
	k = sys.stdin.readline().split()
	if k[0] == 'front':print(front())
	elif k[0] == 'back':print(back())
	elif k[0] == 'pop_front':print(pop_front())
	elif k[0] == 'pop_back':print(pop_back())
	elif k[0] == 'size':print(size())
	elif k[0] == 'empty':print(empty())
	elif k[0] == 'push_front':
		push_front(k[1])
	elif k[0] == 'push_back':
		push_back(k[1])