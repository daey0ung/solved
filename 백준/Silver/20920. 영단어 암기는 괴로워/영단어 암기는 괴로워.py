import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {}

for _ in range(N):
    a = input().strip()
    if len(a) >= M:
        words[a] = words.get(a, 0) + 1
    
W = sorted(words, key=lambda x : (-words[x], -len(x), x))
print(*W, sep='\n')