# 미로만들기 - BFS

import sys
import heapq
N = int(sys.stdin.readline())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, sys.stdin.readline().strip())))


def daikstra():
    while q:
        cost, y, x = heapq.heappop(q)
        if cost > visited[y][x][1]:
            continue
        ty = [-1, 0, 1, 0]
        tx = [0, 1, 0, -1]
        for i in range(4):
            tempy = y + ty[i]
            tempx = x + tx[i]
            if 0 <= tempy < N and 0 <= tempx < N:
                v = visited[tempy][tempx][0]  # 현재 visited 했는지 여부
                b = visited[y][x][1]  # 이전 경로까지의 가중치
                if not v:
                    if not rooms[tempy][tempx]:  # 검은 방이면
                        visited[tempy][tempx] = [1, b+1]
                        heapq.heappush(q, [b+1, tempy, tempx])
                    else:  # 흰 방이면
                        visited[tempy][tempx] = [1, b]
                        heapq.heappush(q, [b, tempy, tempx])


# visited 여부와 해당 위치까지의 검은 방 통과 개수
visited = [[[False, 0] for _ in range(N)] for _ in range(N)]
q = [[0, 0, 0]]  # 검은 방 통과 가중치, y, x
visited[0][0] = [0, 0]
daikstra()
print(visited[N-1][N-1][1])
