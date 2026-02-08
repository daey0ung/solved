import sys
input = sys.stdin.readline

# DP 테이블 초기화: N의 최대 범위(1000)만큼 0으로 채움
A = [0]* 1001

# 초기 상태 설정
A[1] , A[2] = 1, 3

# 보텀업(Bottom-up) DP: 점화식을 이용하여 3부터 1000까지 미리 계산
for i in range(3,1001):
    A[i] = (A[i-1] + 2 * A[i-2]) % 10007

N = int(input())
print(A[N])