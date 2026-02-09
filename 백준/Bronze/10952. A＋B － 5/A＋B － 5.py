# 10952번
# 반복 횟수가 없어 무한 반복으로
while True:
    # 입력값 2개 받기
    a, b = map(int, input().split())
    
    # 입력값이 모두 0이면 종료
    if a == b == 0:
        break
    
    # a+b 출력
    print(a+b)