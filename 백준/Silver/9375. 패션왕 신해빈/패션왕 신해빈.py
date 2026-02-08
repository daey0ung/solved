import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 의상 종류별 개수를 저장할 딕셔너리
    category = {}

    N = int(input())

    for _ in range(N):
        _, c = input().split() # 의상 이름은 필요 없으므로 언더바(_)로 처리하고 종류(c)만 저장
        category[c] = category.get(c, 0) + 1 # 의상의 종류가 있으면 그 값을 가져오고 없으면 0

    answer = 1

    for val in category.values():
        # +1의 이유: 각 의상 종류별로 입지 않는 경우를 포함하여 계산
        answer *= (val+1)

    # -1의 이유: 아무것도 입지 않은 알몸상태 1가지를 제외한 후 출력
    print(answer-1)