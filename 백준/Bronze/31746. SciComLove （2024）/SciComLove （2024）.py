import sys
input = sys.stdin.readline

S = "SciComLove"

N = int(input())

if N%2 == 0:
    print(S)
else:
    print(S[::-1])