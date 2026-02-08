import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
prime = []

for i in range(M, N+1):
    if i < 2:
        continue
    j = 2
    is_prime = True
    while j * j <= i:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        prime.append(i)

if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)