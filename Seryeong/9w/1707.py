# 이분 그래프 - 그래프 탐색
import sys
sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline())


def bfs(V):
    flag = 'YES'
    while q:
        cur = q.pop(0)
        graph[cur].sort()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                if visited[cur] == 1:
                    visited[i] = 2  # 인접한 노드와 다르게 색칠
                else:
                    visited[i] = 1
            else:  # 이미 가본 적 있음
                if visited[cur] == visited[i]:
                    flag = 'NO'
                    break
    return (flag)


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    if V == 1:
        print('YES')
    else:
        visited[0] = 1
        flag = 'YES'
        while 0 in visited and flag == 'YES':
            for i in range(V+1):  # 여러 그래프가 떨어져있을 경우
                if not visited[i]:
                    q = [i]
                    visited[i] = 1
                    if bfs(V) == 'NO':
                        flag = 'NO'
        print(flag)
