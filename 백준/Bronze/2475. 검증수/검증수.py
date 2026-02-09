a = input().split()
# print(a)
a_sum = 0
for i in a:
    a_sum += int(i)**2
print(a_sum%10)