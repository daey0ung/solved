A, B = map(int, input().split())

N = A//B
M = A%B
print(f'{N}', end='')

if M:
    print('.', end='')
    
    for _ in range(1000):
        if M == 0:
            break

        M *= 10
        print(M//B, end='')
        M = M%B