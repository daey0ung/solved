import sys
input = sys.stdin.readline

N = int(input())
A = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for b in range(y, y+h):
        A[b][x:x+w] = [i]*w

answer = [0]*(N+1)
for row in A:
    for v in row:
        if v:
            answer[v] += 1

for i in range(1, N+1):
    print(answer[i])