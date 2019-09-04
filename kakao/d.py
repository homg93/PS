food_times = [3, 1, 2]
k = 5
def solution(food_times, k):
	len_f = len(food_times)
	sum_f = sum(food_times)
	d_time = k
	cal_len = len_f
	cal_i = 0
	sf = sorted(food_times)
	if len_f > k:
		return k+1
	if sum_f <= k:
		return -1
	dp_i = 0
	dp_value
	d_time = 0
	while(d_time <= k ):
		if dp_i == 0:
			d_time = (sf[dp_i])*cal_len
		else:
			d_time = d_time - (sf[dp_i] - sf[dp_i-1])*cal_len
		if d_time < 0:
			break
		sf_cnt = sf.count(sf[dp_i])
		dp_i += sf_cnt
		cal_len -= sf_cnt
	cal_len
	lst = []
	for i in range(len_f-1,-1,-1):
		if food_times[i] >= sf[dp_i]:
			lst.append(i+1)
	if len(lst) != 0:
		return lst[()]



	

	i = 0
	while(k > 0):
		if i == len_f:
			i = 0
		if food_times[i] == 0:
			k -= 1
			continue
		food_times[i] -= 1
		i += 1
		k -= 1
	answer = i
	return answer
print(solution(food_times, k))