from functools import reduce
# v = [[1, 4], [3, 4], [3, 10]]
v= [[1, 1], [2, 2], [1, 2]]
def solution(v):
	answer = []
	x,y = 0,0

	xv,yv = [],[]
	for i in range(3):
		xv.append(v[i][0])
	for i in range(3):
		yv.append(v[i][1])
	for i in range(3):
		if xv.count(xv[i]) == 1:
			x = xv[i]
		if yv.count(yv[i]) == 1:
			y = yv[i]
	answer.append(x)
	answer.append(y)
	return answer
print(solution(v))
