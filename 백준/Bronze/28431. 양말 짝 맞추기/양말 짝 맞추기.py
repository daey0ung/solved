import sys
input = sys.stdin.readline

answer = 0

for _ in range(5):
    N = int(input())
    answer = answer ^ N

print(answer)