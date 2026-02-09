# 10951번
import sys
# 반복 횟수가 없어 무한 반복으로
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break