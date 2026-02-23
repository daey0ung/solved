import sys
input = sys.stdin.readline

N= int(input())

users = set()
users_count = 0

for _ in range(N):
    S = input().strip()
    if S == 'ENTER':
        users.clear()
    else:
        if S not in users:
            users.add(S)
            users_count += 1
        
print(users_count)