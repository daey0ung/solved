# 25304번
# 영수증 총 금액
X = int(input())

# 영수증에 적힌 구매한 물건의 종류의 수
N = int(input())

# 구매한 물건 가격 저장 변수
s = 0

# N번 반복하여 물건의 가격과 개수 받기
for i in range(N):
    a,b = map(int,input().split())
    s += a*b

# 가격 확인
if X == s:
    print('Yes')
else:
    print('No')
