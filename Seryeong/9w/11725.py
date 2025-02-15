# 트리의 부모 찾기 - 그래프 탐색
import sys
nodeNum = int(sys.stdin.readline())  # 노드의 수

graph = [[] for _ in range(nodeNum + 1)]
for _ in range(nodeNum-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (nodeNum + 1)


def dfs(node):
    graph[node].sort()  # 갈 수 있는 곳 중에 가기
    for i in graph[node]:
        if not visited[i]:
            visited[i] = node  # 방문 시에 부모 표시
            dfs(i)


visited[1] = 1
dfs(1)
for i in range(2, nodeNum + 1):
    print(visited[i])
