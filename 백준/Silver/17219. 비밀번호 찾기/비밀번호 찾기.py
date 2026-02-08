import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_L = {k: v for k, v in (input().split() for _ in range(N))}

for _ in range(M):
    print(N_L[input().rstrip()])