N = int(input())
l = [[0]*100 for _ in range(100)]
for i in range(N):
    a, b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            l[x][y] = 1

print(sum(row.count(1) for row in l))