import sys
test = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

def make_heap(x):
	for k in reversed(range(len(x)//2)):
		print(k)
		heapify(x, len(x), k)

def heapify(x,n,k):
	left = 2*k +1
	right = 2*k +2

	if(x[k] > x[left] and left <n):
		m = k
	else:
		m = left

	if(right < n and x[m]< x[right]):
		m = right
	if k != m:
		x[k], x[m] = x[m],x[k]
		k = m
		heapify(x,n,k)

def heap_sort(x):
	make_heap(x)
	n = len(x)
	for k in range(len(x)-1):
		x[0], x[n-1] = x[n-1], x[0]
		n = n-1
		heapify(x,n,0)

heap_sort(test)
for i in test:
	print(i)