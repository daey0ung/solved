import sys
input = sys.stdin.readline

N = int(input())

# 제곱수가 1개인 경우
if int(N**0.5)**2 == N:
    print(1)
    exit()

# 제곱수가 2개인 경우
for i in range(1, int(N**0.5)+1):
    rest = N - i*i
    if int(rest**0.5)**2 == rest:
        print(2)
        exit()


while N % 4 == 0:
    N //= 4

if N % 8 == 7: # 제곱수가 4개인 경우
    print(4)
    exit()
else: # 제곱수가 3개인 경우
    print(3)