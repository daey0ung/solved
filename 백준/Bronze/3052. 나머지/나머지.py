l = []
for _ in range(10):
    a = int(input())%42
    if a not in l:
        l.append(a)
print(len(l))