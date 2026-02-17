S = input().strip()
set1 = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        set1.add(S[i:j])
print(len(set1))