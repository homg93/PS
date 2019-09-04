import sys

def chess(n,m):
	count = 0
	ch = []
	for i in range(n):
		ch.append(sys.stdin.readline().rstrip())

	n_start = n-8+1
	m_start = m-8+1

	rank = []

	for nn in range(n_start):
		for mm in range(m_start):
			w_cnt = 0
			b_cnt = 0
			for i in range(nn, nn+8):
				for j in range(mm, mm+8):
					cal = (i+j)%2
					if(ch[i][j] == 'W' and cal == 0):
						w_cnt += 1
					elif(ch[i][j] == 'B' and cal == 1):
						b_cnt += 1
			rank.append(min(w_cnt+b_cnt,64 - w_cnt - b_cnt))
	rank.sort()
	print(rank[0])

if __name__ == '__main__':
	n,m = map(int,sys.stdin.readline().split())
	chess(n,m)