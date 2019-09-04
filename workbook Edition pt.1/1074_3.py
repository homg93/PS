import sys
n,r,c = map(int,sys.stdin.readline().split())
result = 0

def recursion(x,y,mylen):
    global result  
    if(x==r and y==c):
        print(result)
        return

    if(mylen==1):
        result += 1
        return

    if (x<=r and r<x+mylen) and (y<=c and c<y+mylen) == 0:
        # print(result)
        result += int(mylen*mylen)
        # print(result)

    recursion(x,y,mylen/2);
    recursion(x,y+mylen/2,mylen/2);
    recursion(x+mylen/2,y,mylen/2);
    recursion(x+mylen/2,y+mylen/2,mylen/2);

recursion(0,0,pow(2,n));
