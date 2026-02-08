import sys
input = sys.stdin.readline

N = list(map(int, input().split()))

if sum(N) - max(N) > max(N):
    print(sum(N))
else:
    print(2*(sum(N) - max(N))-1)