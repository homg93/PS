n = int(input())
for i in range(n):
	for j in range(n):
		if (j//3)%3 == 1 and (i//3)%3 == 1:
			print(' ',end='')
		elif (j//9)%9 == 1 and (i//9)%9 == 1:
			print(' ',end='')
		elif(i%3 ==1 and j%3 ==1):
			print(' ',end='')
		else:
			print('*',end='')
	print("")


"""======================================================"""

# import sys

# num = int(input())

# def star(i, j):
#     while(i != 0):
#         # 몫이 1인 경우
#         if(i % 3 == 1 and j % 3 == 1):
#             sys.stdout.write(' ')
#             return None
#         # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
#         i = i // 3
#         j = j // 3
#     sys.stdout.write('*')

# for i in range(num):
#     for j in range(num):
#             star(i, j)
#     sys.stdout.write('\n')