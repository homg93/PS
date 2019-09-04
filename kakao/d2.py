food_times = [1,10,1,20,2,30,1,8]
# food_times = [3,1,2]
food_times = [2,2,2,2,2,3,3,4]
k = 7
# k = 20

def solution(food_times, k):
	d_time = 0
	li = 0
	s_time = sorted(food_times)
	len_f = len(food_times)
	mylist = []
	for i in range(len_f):
		if i == 0:
			d_time += s_time[i]*len_f
		else:
			d_time += (s_time[i]-s_time[i-1])*(len_f-i)
		if d_time > k:
			li = i-1
			break
	if d_time <= k:
		return -1

	# print(s_time[li])
	for i in range(len_f-1,-1,-1):
		if food_times[i] > s_time[li]:
			mylist.append(i+1)
	len_ml = len(mylist)
	# print(mylist)
	if len_ml != 0:
		return mylist[(d_time-k)%len_ml]
	else:
		return k%len_f + 1
print(solution(food_times, k))
