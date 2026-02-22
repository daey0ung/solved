N = int(input())
x = 0
for _ in range(N):
    i, j = map(int, input().split())
    if i == 1:
        x += j
    else:
        x -= j
        if x >= 0:
            continue
        else:
            print('Adios')
            exit()
print('See you next month')