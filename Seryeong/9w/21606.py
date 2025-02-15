# 아침 산책 - 그래프 탐색(73점)
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())  # 정점의 수
# 실내외 여부(1 -> 실내, 0 -> 실외)
A = list(map(int, list(sys.stdin.readline().strip())))

graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0


def dfs(node):
    global cnt
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            # print('새로운 길')
            if A[i-1] == 0:  # 실외면 더 탐색
                # print('실외다 가야지!')
                dfs(i)
            else:  # 실내면 그만 탐색
                # print('실내다 들어가야지!')
                cnt += 1


for i in range(1, N + 1):
    if A[i-1] == 1:  # 시작점은 실내
        visited = [False] * (N + 1)
        dfs(i)

print(cnt)
