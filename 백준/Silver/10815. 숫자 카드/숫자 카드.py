N = int(input())
D = {i:1 for i in list(map(int, input().split()))}

M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i in D.keys():
        print(D[i], end=' ')
    else:
        print(0, end=' ')