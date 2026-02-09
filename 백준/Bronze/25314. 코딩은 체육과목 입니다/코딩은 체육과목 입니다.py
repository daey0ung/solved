# 25314번
# 문제의 정수 N
N = int(input())

# long을 담을 빈 문자열 생성
s = ''

# 4로 나눈 몫만큼 반복
for i in range(N//4):
    s += 'long '

s += 'int'

# 정답 출력
print(s)