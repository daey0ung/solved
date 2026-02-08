import sys
input = sys.stdin.readline

N = int(input())
N_L = list(map(int, input().split()))
cnt = {}

for i in N_L:
    cnt[i] = cnt.get(i, 0) + 1
    
M = int(input())
M_L = list(map(int, input().split()))

for i in M_L:
    print(cnt.get(i, 0), end=' ')