N = int(input())
arr = [0] *10001
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x,y):
        arr[i] = 1

print(sum(arr))