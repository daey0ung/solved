T = int(input())

for i in range(T):
    answer = ''
    R, S = input().split()
    for j in range(len(S)):
        answer += S[j] * int(R)
    print(answer)