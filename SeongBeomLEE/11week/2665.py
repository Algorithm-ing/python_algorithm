import sys
import heapq
input = sys.stdin.readline
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(input()))

visited = [[False] * N for _ in range(N)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
moves = []
heapq.heappush(moves, (0, 0, 0))
answer = 987654321
visited[0][0] = True
while moves:
    cnt, row, col = heapq.heappop(moves)
    if row == N - 1 and col == N - 1:
        answer = min(answer, cnt)
        break
    for dx, dy in zip(dxs, dys):
        x, y = row + dx, col + dy
        if x >= 0 and y >= 0 and x < N and y < N and not visited[x][y]:
            visited[x][y] = True
            heapq.heappush(moves, (cnt if maps[x][y] == "1" else cnt + 1, x, y))
print(answer)