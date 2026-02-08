import sys
input = sys.stdin.readline

N = int(input())
L = set(map(int,input().split()))

print(N - len(L))