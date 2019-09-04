matrix = [[row for col in range(2)] for row in range(3,50)]
# print(matrix)

# matrix = [[row for col in range(2)] for row in range(3,10)]
# matrix = [[col for col in range(10)] for row in range(10)]

m_len = len(matrix)
for i in range(m_len):
	a= i+3
	share5 = int(a/5)
	rest5  = a%5
	if(rest5 == 0):
		matrix[i][1] = share5
		# print(share5)
	else:
		share3 = int(rest5/3)
		rest3 = rest5%3
		result = share5 + share3
		if(rest3 == 0):
			# print(result)
			matrix[i][1] = result
		else:
			if(a%3 == 0):
				# print(int(a/3))
				matrix[i][1] = int(a/3)
			else:
				# print(-1)
				matrix[i][1] = -1
print(matrix)