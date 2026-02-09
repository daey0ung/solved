N,M= map(int, input().split())
list_10810 = [0]*N
for _ in range(M):
    i,j,k = map(int, input().split())
    list_10810[i-1:j] = [k for _ in range(i-1,j)]
print(*list_10810)