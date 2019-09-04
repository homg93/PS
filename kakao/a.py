record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
	save = {}
	answer = []
	for i in range(len(record)):
		a = record[i].split()
		if a[0] == "Enter":
			save[a[1]] = a[2]
		elif a[0] == "Change":
			save[a[1]] = a[2]

	for i in range(len(record)):
		a = record[i].split()
		if a[0] == "Enter":
			answer.append("%s님이 들어왔습니다."%save[a[1]])
		elif a[0] == "Leave":
			answer.append("%s님이 나갔습니다."%save[a[1]])
	return answer

def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

print(solution2(record))