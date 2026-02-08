import sys
input = sys.stdin.readline
N =int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

A.sort()
for i in A:
    print(*i)