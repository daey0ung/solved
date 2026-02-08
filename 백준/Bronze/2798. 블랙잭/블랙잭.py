import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

best = 0
for x, y, z in combinations(A, 3):
    s = x + y + z
    if s <= M and s > best:
        best = s

print(best)
