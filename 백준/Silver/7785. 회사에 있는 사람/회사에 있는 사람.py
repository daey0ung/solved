N = int(input())

people = {}
for _ in range(N):
    name, status = input().split()
    if status == 'leave':
        people.pop(name)
    else:
        people[name] = 1

for name in sorted(people.keys(), reverse=True):
    print(name)