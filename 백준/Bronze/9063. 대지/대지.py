import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
    sys.exit()

x = []
y = []

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

min_x, max_x = min(x), max(x)
min_y, max_y = min(y), max(y)

len_x = max_x - min_x
len_y = max_y - min_y

print(len_x * len_y)