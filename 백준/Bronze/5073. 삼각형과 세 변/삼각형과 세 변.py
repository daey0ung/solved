import sys
input = sys.stdin.readline

while True:
    N = list(map(int, input().split()))

    if sum(N) == 0:
        sys.exit()

    if sum(N) - max(N) <= max(N):
        print('Invalid')
    else:
        if len(set(N)) == 1:
            print('Equilateral')
        elif len(set(N)) == 2:
            print('Isosceles')
        else:
            print('Scalene')

            