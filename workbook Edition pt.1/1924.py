import sys

def date2(x,y):
	day31 = [1,3,5,7,8,10,12]
	day30 = [4,6,9,11]
	myday = 0
	day = [ 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
	for i in range(x):
		if(i in day31 ):
			myday += 31
		elif( i in day30):
			myday += 30
		elif i == 2:
			myday += 28
	
	myday += y
	a = myday % 7
	print(day[a])


if __name__ == '__main__':
	x, y = map(int, sys.stdin.readline().split())
	date2(x,y)