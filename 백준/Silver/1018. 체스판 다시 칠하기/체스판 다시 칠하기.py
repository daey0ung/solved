import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

answer = 64

for x in range(N - 7):
    for y in range(M - 7):
        cnt_w = 0
        cnt_b = 0

        for i in range(8):
            for j in range(8):
                cur = board[x + i][y + j]

                if (i + j) % 2 == 0:
                    if cur != 'W':
                        cnt_w += 1
                    if cur != 'B':
                        cnt_b += 1
                else:
                    if cur != 'B':
                        cnt_w += 1
                    if cur != 'W':
                        cnt_b += 1
        answer = min(answer, cnt_w, cnt_b)

print(answer)
