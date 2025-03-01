# 최소비용 구하기 - BFS

import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

busMap = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, expense = map(int, sys.stdin.readline().split())
    busMap[start].append([end, expense])

start, end = map(int, sys.stdin.readline().split())


def daikstra():
    while q:
        cost, city = heapq.heappop(q)
        # 지금까지의 최적 비용이 이전에 city 갔을 때의 최적 비용보다 크면 더이상 가지 않고 멈춤
        if cost > visited[city]:
            continue
        for end, expense in busMap[city]:
            newExpense = visited[city] + expense
            # 아직 가본 적 없거나 더 적은 비용으로 갈 수 있으면
            if visited[end] > newExpense:
                heapq.heappush(q, [newExpense, end])
                visited[end] = newExpense
    return


INF = float('inf')
visited = [INF] * (N + 1)
visited[start] = 0
q = [(0, start)]
daikstra()
print(visited[end])
