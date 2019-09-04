import sys
import math
# m,n = map(int, sys.stdin.readline().split())

# for i in range(m,n+1):
# 	cnt = 0
# 	if i == 2:
# 		print(i)
# 	if(i%2):
# 		sep = i//2+1
# 		for j in range(1,sep):
# 			if(i%j == 0):
# 				cnt += 1
# 				if(cnt >1):
# 					break
# 		if cnt == 1:
# 			print(i)

# print(math.ceil(math.sqrt(1000)))

def isPrime(num):
	if num == 1: return False

	n = int(math.sqrt(num))
	for k in range(2, n+1):
		if num % k == 0: return 0
	return True

m,n = map(int, sys.stdin.readline().split())
mycnt = 0
for k in range(m,n+1):
	if isPrime(k):
		mycnt += 1
print(mycnt)



# # wiki
# def prime_list(n):
#	 # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#	 sieve = [True] * n

#	 # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#	 m = int(n ** 0.5)
#	 for i in range(2, m + 1):
#		 if sieve[i] == True:		   # i가 소수인 경우 
#			 for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#				 sieve[j] = False

#	 # 소수 목록 산출
#	 return [i for i in range(2, n) if sieve[i] == True]