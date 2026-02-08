import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = {}

for i in range(1, N+1):
    a = input().rstrip()
    answer[i] = a
    answer[a] = i

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(answer[int(q)])
    else:
        print(answer[q])