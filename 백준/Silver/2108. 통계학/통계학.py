import sys
input = sys.stdin.readline

N = int(input())
L = [int(input()) for _ in range(N)]

L.sort()
# print(L)

print(round(sum(L)/len(L)))
print(L[len(L)//2])

D = {}
for i in L:
    D[i] = D.get(i, 0) + 1
mx = max(D.values())
mx_L = []
for i in D:
    if mx == D[i]:
        mx_L.append(i)
mx_L.sort()
if len(mx_L) > 1:
    print(mx_L[1])
else:
    print(mx_L[0])

print(max(L) - min(L))