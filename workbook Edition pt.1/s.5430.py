import sys

def procACLang(Funcs,Arr):
    isRvs = 0
    frontPos = 0
    backPos = len(Arr)
    
    for f in Funcs:
        if f == "R":
            if isRvs == 0:
                isRvs = 1
            else:
                isRvs = 0
        elif f == "D":
            if frontPos >= backPos :
                return "error"
            else:
                if(isRvs == 1):
                    backPos -=1
                else:
                    frontPos +=1
                    
    Arr = Arr[frontPos:backPos]
    
    if isRvs == 1:
        Arr.reverse()
    rtnVal = "[" + ",".join(Arr) + "]"
    return rtnVal

T = int(sys.stdin.readline())
for _ in range(T):
    Funcs = sys.stdin.readline()
    N = int(sys.stdin.readline())
    strArr = sys.stdin.readline()
    sArr = strArr[1:len(strArr)-2]

    Arr = []
    if len(sArr) != 0:
        Arr = sArr.split(",")
    print(procACLang(Funcs,Arr))