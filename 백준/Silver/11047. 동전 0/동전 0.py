import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = [int(input()) for _ in range(N)]
cnt = 0

for i in L[::-1]:
    if i > K:
        continue
        
    if K//i == 0:
        cnt += K//i
        break
    elif K//i > 0:
        cnt += K//i
        K = K%i

print(cnt)