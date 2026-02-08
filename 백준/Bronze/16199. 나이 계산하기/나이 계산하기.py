# 16199.py
import sys
input = sys.stdin.readline

N = list(map(int, input().split()))
M = list(map(int, input().split()))

# 만나이
if (N[1] == M[1] and N[2] > M[2]) or (N[1] > M[1]):
    print(M[0] - N[0] - 1)
else:
    print(M[0] - N[0])

# 세는 나이
print(M[0] - N[0] + 1)

# 연 나이
print(M[0] - N[0])