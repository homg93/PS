import sys

def tile2(n):
	mybool = 1
	for i in range(1,n):
		a[i] = a[i-1]*2 +mybool
		mybool *= -1
	return a[n-1]

n = int(sys.stdin.readline())
a = [1 for _ in range(n+1)]
print(tile2(n)%10007)

#s11727
# a,b,c=1,1,0
# for i in range(int(input())-1):
#     a,b,c=c,a,b
#     a=b+c*2
# print(a%10007)