import sys
input = sys.stdin.readline

# DP 테이블 초기화
dp = [0] * 11

# 기본값 설정
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 점화식 적용
for i in range(4,11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

# 테스트 케이스 입력받기
T = int(input())

for _ in range(T):
    # 정수 입력 받기
    N = int(input())

    # 입력 받은 정수의 방법의 수 출력
    print(dp[N])