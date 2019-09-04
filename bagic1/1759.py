from sys import stdin

def go(l,a,password,i):
	if len(password) == l:
		if check(password):
			print(password)
		return
	if i >= len(a):
		return
	go(l,a,password+a[i],i+1)
	go(l,a,password, i+1)
def check(password):
	ja = 0
	mo = 0
	mo_arr = ['a','e','i','o','u']
	for c in password:
		if c in mo_arr:
			mo += 1
		else:
			ja += 1
	return ja >= 2 and mo >=1

l,c = map(int, stdin.readline().split())
a = sorted(list(map(str, stdin.readline().split())))
go(l,a,"",0)
