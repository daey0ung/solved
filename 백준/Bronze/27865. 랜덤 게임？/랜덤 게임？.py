import sys
import random

input = sys.stdin.readline

N = int(input().strip())

while True:
    guess = random.randint(1, N)
    print("?", guess, flush=True)

    resp = input().strip()
    if resp == 'Y':
        print("!", guess, flush=True)
        break