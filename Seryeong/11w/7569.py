# 토마토 - BFS

import sys
import collections
M, N, H = map(int, sys.stdin.readline().split())

tomatos = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, sys.stdin.readline().strip().split())))
    tomatos.append(temp)


def bfs():

    tz = [0, 0, 0, 0, 1, -1]
    ty = [0, 0, 1, -1, 0, 0]
    tx = [-1, 1, 0, 0, 0, 0]
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            tempz = z + tz[i]
            tempy = y + ty[i]
            tempx = x + tx[i]
            if 0 <= tempz < H and 0 <= tempy < N and 0 <= tempx < M:
                cur_tomato = tomatos[tempz][tempy][tempx]
                if cur_tomato == 0:
                    tomatos[tempz][tempy][tempx] = tomatos[z][y][x] + 1
                    q.append([tempz, tempy, tempx])


q = collections.deque([])
tomatoCnt = 0
emptyCnt = 0
result = None
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 1:
                tomatoCnt += 1
                q.append([z, y, x])
                tomatos[z][y][x] = 1
            elif tomatos[z][y][x] == -1:
                emptyCnt += 1

totalSpace = H * N * M
if tomatoCnt == totalSpace or emptyCnt == totalSpace:  # 토마토가 다 익었거나 아예 없거나
    result = 0
else:  # 다 익어 있지 않았다면
    bfs()
    maxNum = 0  # 다 익을 때까지 최소일수
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatos[z][y][x] == 0:  # 하나라도 안 익었으면
                    result = -1
                    break
                maxNum = max(maxNum, tomatos[z][y][x])
    if result != -1:
        result = maxNum - 1

print(result)
