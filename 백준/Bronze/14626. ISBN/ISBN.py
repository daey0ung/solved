# 14626번
A = list(input())
add_A = 0
answer_mod = False
for i in range(13):
    if A[i] == '*':
        if i%2!=0:
            answer_mod = True
        continue
    add_A += int(A[i]) * (1 if i%2==0 else 3)

if answer_mod:
    for i in range(10):
        if (add_A + (i*3)) % 10 == 0:
            print(i)
            break
else:
    print(10 - add_A % 10)