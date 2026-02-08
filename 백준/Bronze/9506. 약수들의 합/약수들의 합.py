import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break

    N_factor = []
    for i in range(1,N):
        if N % i == 0:
            N_factor.append(i)
    result = ' + '.join(map(str, N_factor))
    if sum(N_factor) == N:
        print(f'{N} = {result}')
    else:
        print(f'{N} is NOT perfect.')