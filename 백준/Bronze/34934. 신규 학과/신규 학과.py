import sys
input = sys.stdin.readline

N = int(input())
dept_d = {}

for _ in range(N):
    a, b = input().split()
    dept_d[int(b)] = a

print(dept_d[2026])