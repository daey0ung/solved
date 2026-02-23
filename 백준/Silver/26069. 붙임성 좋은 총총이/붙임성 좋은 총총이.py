import sys
input = sys.stdin.readline

N= int(input())

users = set()
users.add('ChongChong')

for _ in range(N):
    a, b = input().split()

    if a in users or b in users:
        users.add(a)
        users.add(b)
        
print(len(users))