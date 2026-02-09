N = int(input())
A = list(map(int, input().split()))
for i in A:
    if i == 1:
        N -= 1
        continue

    for j in range(2, i):
        if i % j == 0:
            N -= 1
            break

print(N)