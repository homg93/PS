import sys

def doc():
	end = "END"

	while True:
		mystr = input()
		if(mystr == end):
			break
		print(''.join((reversed(mystr))))

if __name__ == '__main__':
	doc()