import sys
input = sys.stdin.readline

check_list = {
    '2' : 0,'0' : 0,
    '1' : 0, '8' : 0
}

N = list(input().strip())
N_set = set(N)

for i in N_set:
    if i in check_list:
        check_list[i] = N.count(i)
    else:
        print(0)
        exit()
    
if 0 in check_list.values():
    print(1)
elif len(set(check_list.values())) == 1:
    print(8)
else:
    print(2)