import sys
test = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

def quickSort(arr,l,r):
	if l<r:
		p = partition(arr,l,r)
		quickSort(arr,l,p-1)
		quickSort(arr,p+1,r)

def partition(arr,l,r):
	pivot = arr[r]
	i = l-1
	
	for j in range(l,r):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[r] = arr[r], arr[i+1]


	return i+1

quickSort(test,0,len(test)-1)
for b in test:
	print(b)
# st = "123,456,789"
# find = st.rfind(",")
# print(find)
# print(st[:find])