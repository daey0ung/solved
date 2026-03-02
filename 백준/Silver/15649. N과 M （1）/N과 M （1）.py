# 순열
N, M = map(int, input().split())
array = [i for i in range(1,N+1)]
visited = [False for _ in range(len(array))]

def backtrack(arr):
	if len(arr) == M:
		print(*arr, sep=' ',)
		return
	
	for i in range(len(array)):
		if visited[i] == False:
			visited[i] = True
			backtrack(arr + [array[i]])
			visited[i] = False

backtrack([])