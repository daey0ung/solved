import sys
input = sys.stdin.readline

# 계단의 개수
N = int(input())

# 각 계단의 점수(1번부터 index 시작)
S = [0] * 301
for i in range(1, N+1):
    S[i] = int(input())

# 각 계단의 최대 점수 저장 리스트
dp = [0] * 301

# 1번부터 3번계단은 수동입력
dp[1] = S[1]
dp[2] = S[1]+S[2]
dp[3] = max(S[1]+S[3], S[2]+S[3])

# 4번계단부터는 알고리즘 적용
for i in range(4, N+1):
    dp[i] = max(dp[i-3]+S[i-1]+S[i], dp[i-2]+S[i])

print(dp[N])