a = int(input())
b = input()
b_reversed = b[::-1]
# print(a,b)
outputs = 0
for i in range(3):
    print(a*int(b_reversed[i]))
    outputs += int(a*int(b_reversed[i]))*(10**i)
print(outputs)