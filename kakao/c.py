relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
def solution(relation):
	answer = 0
	h = len(relation)
	w = len(relation[0])
	a = [[""]*h for _ in range(w)]
	remove = []
	for i in range(h):
		for j in range(w):
			a[j][i] = relation[i][j]
	print(a)
	for i in range(4):
		ta = set(a[i])
		# temp = set(zip(range(1, N+1), a[i]))
		if len(ta) == h:
			answer+=1
			remove.append(i)
	while len(remove):
		del a[remove.pop()]
	print(a)
	if len(a) == 0 or len(a) == 1:
		return answer
	return answer
print(solution(relation))