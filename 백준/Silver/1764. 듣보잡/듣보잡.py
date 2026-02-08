import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_L = set(input().strip() for _ in range(N))
M_L = set(input().strip() for _ in range(M))

print(len(N_L & M_L))
print('\n'.join(map(str, sorted(N_L & M_L))))