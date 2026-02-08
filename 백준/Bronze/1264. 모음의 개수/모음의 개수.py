import sys
input = sys.stdin.readline
answer_list = ['a','A','e','E','i','I','o','O','u','U']
while True:
    answer = 0
    S = input().strip()
    if S == '#':
        break

    for i in answer_list:
        answer += S.count(i)

    print(answer)