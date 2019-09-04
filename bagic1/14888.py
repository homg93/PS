from sys import stdin

def go(tot,i,plus,minus,mul,div):
	global mymax
	global mymin

	if n == i:
		mymax = max(mymax,tot)
		mymin = min(mymin,tot)
		return
	if plus<0 or minus<0 or mul<0 or div<0:
		return
	if plus>0:
		go(tot+a[i],i+1,plus-1,minus,mul,div)
	if minus>0:
		go(tot-a[i],i+1,plus,minus-1,mul,div)
	if mul>0:
		go(tot*a[i],i+1,plus,minus,mul-1,div)
	if div>0:
		if tot >= 0:
			go(tot//a[i],i+1,plus,minus,mul,div-1)
		else:
			go(-(-tot//a[i]),i+1,plus,minus,mul,div-1)

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
cal = list(map(int, stdin.readline().split()))
mymax = -10**9
mymin = 10**9
go(a[0],1,cal[0],cal[1],cal[2],cal[3])
print(mymax)
print(mymin)