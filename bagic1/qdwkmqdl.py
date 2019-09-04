import sys
while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    land = []
    for _ in range(H):
        land.append(list(map(int, sys.stdin.readline().split())))
    print(land)

from sys import stdin
from collections import deque, Counter
from functools import reduce

n = int(stdin.readline())
a = [list(map(int,list(input()))) for _ in range(n)]
# a = [list(map(int,list(sys.stdin.readline()))) for _ in range(n)]