num = [x for x in range(1,246913)]#2n개의 리스트
num.insert(0,1)#리스트 맨 앞에 1 삽입
for i in range(2,246913):#2~2*n 보다 큰 배수
    j=2 #자기 자신보다 큰 배수를 구하기 위한 값
    while 246912>=i*j: #배수의 값은 2n보다 작거나 같게.
        num[i*j] = 1 #배수는 1로
        j+=1 #다음 배수
# while True: #소수를 처음에 구해놓는다. 1~123456*2까지
for n in range(1,123457):
    if n<=0:
        break
    count = 0
    for l in num:
        if l != 1 and n<l and l<=2*n:
            count +=1
    print(count)