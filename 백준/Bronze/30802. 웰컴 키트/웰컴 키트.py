# 30802번
N = int(input())
A = list(map(int, input().split()))
T, P = map(int, input().split())

T_set = 0
P_set = 0
P_rest = 0

for i in A:
    T_set += i//T
    if i%T > 0:
        T_set += 1

P_set = N // P
P_rest = N % P

print(T_set)
print(P_set, P_rest)