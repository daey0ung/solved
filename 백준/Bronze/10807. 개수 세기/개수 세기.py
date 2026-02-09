# 10807번
# 받을 정수의 개수
N = int(input())

# 정수를 리스트로 받기
num_list = list(map(int, input().split()))

# 리스트에서 찾으려는 정수 v 받기
v = int(input())

# 리스트에서 v의 개수 구하기
print(num_list.count(v))