# 미로탐색 - BFS
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())  # N개의 줄 M개의 정수
maze = []

for _ in range(N):
    maze.append(list(map(int, (list(sys.stdin.readline().strip())))))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
q = [[0, 0]]


def bfs(starty, startx):
    global visited, cnt
    if starty == N and startx == M:
        return
    for i in range(4):  # 위, 오른쪽, 아래, 왼쪽 순회
        tempy = starty + dy[i]
        tempx = startx + dx[i]
        if 0 <= tempy < N and 0 <= tempx < M:  # 미로 범위를 넘는지 확인
            if maze[tempy][tempx] and not visited[tempy][tempx]:  # 갈 수 있는 곳이며 안 간 곳인지 확인
                q.append([tempy, tempx])
                visited[tempy][tempx] = visited[starty][startx] + 1
    while q:
        y, x = q.pop(0)
        bfs(y, x)


visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
bfs(0, 0)
print(visited[N-1][M-1])
