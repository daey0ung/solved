# 2738번
n, m = map(int, input().split())
a = []
for _ in range(2):
    for i in range(n):
        a.append(list(map(int, input().split())))
b = a[n:]
a= a[:n]
for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=' ')
    print()