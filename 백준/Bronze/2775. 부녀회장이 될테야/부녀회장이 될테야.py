import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    print(math.comb(n + k, k + 1))