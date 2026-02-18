M = 246912

primes = [0, 0] + [1] * (M-1)
for i in range(2, int(M**0.5)+1):
    if primes[i]:
        for j in range(i*i, M+1,i):
            primes[j] = 0

while True:
    N = int(input())
    if N == 0:
        break

    print(sum(primes[N+1:2*N+1]))