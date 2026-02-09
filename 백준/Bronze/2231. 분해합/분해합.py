N = int(input())
answer = 0

start = max(0, N - 9 * len(str(N)))  # 생성자 후보의 하한

for i in range(start, N):
    s = i + sum(map(int, str(i)))
    if s == N:
        answer = i
        break

print(answer)