import sys

def big2(a):
	a_len = len(a)
	top = 0
	for i in range(a_len):
		for j in range(i+1,a_len):
			if(a[i] < a[j]):
				tmp = a[i]
				a[i] = a[j]
				a[j] = tmp
	print(a[1])

if __name__ == '__main__':
	a = list(map(int, sys.stdin.readline().split()))
	big2(a)
