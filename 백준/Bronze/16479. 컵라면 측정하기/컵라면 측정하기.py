k = int(input())
a, b = map(int, input().split())
answer = k**2 - ((a-b)/2)**2
print(answer)