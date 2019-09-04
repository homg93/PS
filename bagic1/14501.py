from sys import stdin

def go(n,t,p,tot,i):
	global max_p
	if n ==i:
		if max_p < tot:
			max_p = tot
		return
	if n < i:
		return

	go(n,t,p,tot+p[i],i+t[i])
	go(n,t,p,tot,i+1)
	return


p,t =[],[]
n = int(stdin.readline())
for i in range(n):
	t_, p_ = map(int,stdin.readline().split())
	t.append(t_)
	p.append(p_)
max_p = 0
go(n,t,p,0,0)
print(max_p)

# inf = -10**9
# n = int(input())
# t = [0]*(n+1)
# p = [0]*(n+1)
# for i in range(1, n+1):
#     t[i],p[i] = map(int,input().split())
# ans = 0
# def go(day, s):
#     global ans
#     if day == n+1:
#         ans = max(ans, s)
#         return
#     if day > n+1:
#         return
#     go(day+1, s)
#     go(day+t[day], s+p[day])

# go(1, 0)
# print(ans)