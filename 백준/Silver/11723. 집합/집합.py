import sys

input = sys.stdin.readline

N = int(input())
answer = set()

for _ in range(N):
    A = input().split()
    # print(A)
    command = A[0]

    if command == 'all':
        answer = set([i for i in range(1,21)])
    elif command == 'empty':
        answer = set()
    elif command == 'add':
        answer.add(int(A[1]))
    elif command == 'remove':
        answer.discard(int(A[1]))
    elif command == 'check':
        print(1 if int(A[1]) in answer else 0)
    else:
        if int(A[1]) in answer:
            answer.discard(int(A[1]))
        else:
            answer.add(int(A[1]))