# 바이러스 - 그래프 탐색
import sys
comNum = int(sys.stdin.readline())  # 컴퓨터의 수
con = int(sys.stdin.readline())  # 연결되어 있는 컴퓨터 쌍의 수

graph = [[False] * (comNum + 1) for _ in range((comNum + 1))]
for _ in range(con):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (comNum + 1)  # 방문 기록
q = [1]
visited[1] = True
cnt = 0


def bfs():
    global cnt
    while q:
        cur = q.pop(0)
        for i in range(1, comNum + 1):
            if not visited[i] and graph[cur][i]:
                q.append(i)
                visited[i] = True
                cnt += 1


bfs()
print(cnt)
