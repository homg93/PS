relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
def possi(vec, now):
	for i in range(len(vec)):
		print(vec[i],now,vec[i]&now,end=' ')
		print()
		if (vec[i]&now) == vec[i]:
			return False
	print("PLUS")
	return True

def solution(relation):
	n = len(relation)
	m = len(relation[0])
	ans = []
	for i in range(1,1<<m):
		s = set()
		for j in range(n):
			now = ""
			for k in range(m):
				if i&(1<<k):
					now+=relation[j][k]
					# print(i,j,k,1<<k,end =' ')
					# print(i&(1<<k))
			# print(now)
			# print("============")
			s.add(now)
		# print(len(s))
		# print(n and possi(ans,i))
		# print("@@@@@@@@@@@@")
		if len(s) == n and possi(ans,i):
			ans.append(i)
			print(ans,i,end=' ')
			print("OKOKOKOK")

	return len(ans)
print(solution(relation))

