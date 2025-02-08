# DFS(깊이 우선 탐색)와 BFS(너비 우선 탐색)
import sys
import collections
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())
input = []
for _ in range(M):
    input.append(list(map(int, sys.stdin.readline().split())))

## 각 정점 번호에 연결된 정점의 번호들 리스트(정렬되어 있어야 함)
g = [[] for _ in range(N+1)]
for i in input:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])

for i in g:
    i.sort()

## DFS ===========================================
## 0번째 자리도 만들어줘야 함
v = [0]*(N+1)
output1 = []
def DFS(graph, start, visited):
    ## 방문표시
    visited[start] = 1
    # print(start, end=' ')
    output1.append(str(start))
    ## 🚨 이미 여기서 종료 조건이 들어감
    for i in graph[start]:
        ## 방문 안 했으면 탐색 시작
        if visited[i] == 0:
            DFS(graph, i, visited)

DFS(g, V, v)
## BFS ===========================================
q = collections.deque([])
vi = [0]*(N+1)
output2 = []
def BFS(graph, start, visited):
    ## 방문표시
    visited[start] = 1
    # print(start, end=' ')
    output2.append(str(start))
    for i in graph[start]:
        q.append(i)
    while q:
        nstart = q.popleft()
        if visited[nstart] == 0:
            BFS(graph, nstart, visited)

BFS(g, V, vi)

print(' '.join(output1))
print(' '.join(output2))