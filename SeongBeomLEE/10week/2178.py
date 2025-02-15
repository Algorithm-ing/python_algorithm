import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(input()))

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우
visited = [[False] * M for _ in range(N)]
checks = deque([[0, 0, 1]])
visited[0][0] = True
while checks:
    x, y, answer = checks.popleft()
    if x == N - 1 and y == M - 1:
        break
    for dx, dy in moves:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if maps[x + dx][y + dy] == "1" and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = True
                checks.append([x + dx, y + dy, answer + 1])
print(answer)
