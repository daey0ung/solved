# 중복 순열
N, M = map(int, input().split())
array = [i for i in range(1,N+1)]

def backtrack(arr):
	if len(arr) == M:
		print(*arr, sep=' ',)
		return
	
	for i in range(len(array)):
		backtrack(arr + [array[i]])

backtrack([])