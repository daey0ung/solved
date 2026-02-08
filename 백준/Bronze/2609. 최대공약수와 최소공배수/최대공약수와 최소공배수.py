A, B = map(int, input().split())
end = min(A,B)
mul=1
for i in range(2, end+1):
    while (A%i==0) and (B%i==0):
        mul*=i
        A = A//i
        B = B//i

print(mul)
print(mul*A*B)