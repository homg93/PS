import sys

def cal_avg(n):
	rslt = []
	for i in range(n):
		avg = 0
		cnt = 0
		std = list(map(int, sys.stdin.readline().split()))
		
		avg = sum(std[1:])/std[0]
		# for i in range(1,std[0]):
		# 	avg += std[i]
		# avg = avg/std[0]*100
		for j in std[1:]:
			if j>avg:
				cnt += 1
		result = round(cnt/std[0] * 100,3)
		rslt.append(result)
		# print("%.3f" % round(cnt/std[0] * 100,3))
	for i in range(n):
		print("%.3f%%" % rslt[i])




		rslt.append(avg)

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	cal_avg(n)