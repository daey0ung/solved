import sys
input = sys.stdin.readline
k, s= map(int, input().split())

sentence = input().strip()
for w in sentence:
    if w.isupper():
        a_w = (ord(w)-ord('A')+k) % 26 + ord('A')
        print(chr(a_w), end='')
    elif w.islower():
        a_w = (ord(w)-ord('a')+k) % 26 + ord('a')
        print(chr(a_w), end='')
    else:
        print(w, end='')