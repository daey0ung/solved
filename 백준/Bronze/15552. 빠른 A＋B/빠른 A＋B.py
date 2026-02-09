# 15552번
import sys

# 반복 횟수
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    # 띄어쓰기로 구분한 여러 개 숫자를 한 줄에 입력받고 리스트에 저장
    a = list(map(int, sys.stdin.readline().split()))
    
    # 리스트 더하기
    print(sum(a))