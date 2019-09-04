import sys
def score(n):
	sc = list(map(int,sys.stdin.readline().split()))
	avg = 0

	sc.sort(reverse = False)

	for i in range(n):
		sc[i] = sc[i]/sc[n-1]*100
		avg += sc[i]
	avg /= n
	print(avg)

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	score(n)
# print(ord(input()))