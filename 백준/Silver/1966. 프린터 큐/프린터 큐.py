from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        mx = max(q)
        front = q.popleft()
        M -= 1

        if mx == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            q.append(front)
            if M < 0:
                M = len(q) - 1