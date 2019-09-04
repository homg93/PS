N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
	answer = []
	failure = [0]*N
	a = [0]*(N+1)
	slen = len(stages)
	hit_user = slen
	for i in stages:
		a[i-1] += 1

	for i in range(N):
		failure[i] = a[i] / hit_user
		hit_user -= a[i]
		if hit_user == 0:
			hit_user = 1

	temp = 0
	temp = tuple(zip(range(1, N+1), failure))
	temp = sorted(temp,key=lambda x:x[1],reverse=True)
	for i in temp:
		answer.append(i[0])
	return answer
print(solution(N, stages))