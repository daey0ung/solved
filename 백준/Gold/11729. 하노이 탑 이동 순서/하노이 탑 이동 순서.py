def hanoi(n, from_pos=1, to_pos=3, aux_pos=2):
    if n == 1:
        print(from_pos, to_pos)
        return
    
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

N= int(input())
print(2**N-1)
hanoi(N)