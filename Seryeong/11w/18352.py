# 특정 거리의 도시 찾기 - BFS

import sys
N, M, K, X = map(int, sys.stdin.readline().split())

roadMap = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    roadMap[a].append(b)  # 단방향 그래프

kCity = []


def bfs():
    while q:
        city = q.pop(0)
        for i in roadMap[city]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[city] + 1
                if visited[i]-1 == K:  # 최단 거리가 K이면
                    kCity.append(i)

    return


visited = [False for _ in range(N+1)]
q = [X]
visited[X] = 1
bfs()

if len(kCity) == 0:
    print(-1)
else:
    kCity.sort()
    for i in kCity:
        print(i)
