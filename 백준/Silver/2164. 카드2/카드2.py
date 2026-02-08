import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
L = [i for i in range(1,N+1)]
q = deque(L)

while len(q) >1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0])