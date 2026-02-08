import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N -= 1
M -= 1

N_X =  N // 4
N_Y = N % 4

M_X = M // 4
M_Y = M % 4

print(abs(M_X - N_X) + abs(M_Y - N_Y))