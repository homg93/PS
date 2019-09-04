import sys

def myplus():
	while 1:
		lit = list(map(int,sys.stdin.readline().rstrip().split()))
		result = sum(lit[:])
		if (not result):
			break
		print(result)

if __name__ == '__main__':
	myplus()
# def myplus(t):
# 	for i in range(t):
# 		lit = list(map(int,sys.stdin.readline().rstrip().split()))
# 		print(sum(lit[:]))

# if __name__ == '__main__':
# 	t = int(sys.stdin.readline())
# 	myplus(t)
