A, B, V = map(int, input().split())
C = A-B # 일일 증가량
D = V-A # 남은 거리
E = D//C # 소요 기간(일)
rest = D%C # 남은 거리 여부
day=0 # 소요 기간 저장
if D==0: # 첫날에 도착시
    day=1
else:
    if rest == 0: # 남은 거리가 없다면
        day = E+1 # 소요 기간 + 첫날
    else: # 남은 거리가 있다면
        day = E+2 # 소요 기간 + 첫날 + 남은 거리 가는 하루
print(day)