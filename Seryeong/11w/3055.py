# 탈출 - BFS

import sys
R, C = map(int, sys.stdin.readline().split())

tiddup = []
for _ in range(R):
    tiddup.append(list(sys.stdin.readline().strip()))

waterq = []
hedgehogq = []
beaver = []
for y in range(R):
    for x in range(C):
        loc = tiddup[y][x]
        if loc == 'S':
            hedgehogq.append([y, x])
        elif loc == '*':
            waterq.append([y, x])
        elif loc == 'D':
            beaver = [y, x]

result = 0


def bfs(wq, hq, time):
    global result
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    # 물 먼저, 고슴도치 나중에
    nextWq = []
    while wq:
        wy, wx = wq.pop()
        for i in range(4):
            tempy = wy + dy[i]
            tempx = wx + dx[i]
            if 0 <= tempy < R and 0 <= tempx < C:
                if tiddup[tempy][tempx] == ".":
                    tiddup[tempy][tempx] = '*'
                    nextWq.append([tempy, tempx])

    nextHq = []
    while hq:
        hy, hx = hq.pop()
        for i in range(4):
            tempy = hy + dy[i]
            tempx = hx + dx[i]
            if 0 <= tempy < R and 0 <= tempx < C:
                if tiddup[tempy][tempx] == ".":
                    tiddup[tempy][tempx] = 'S'
                    nextHq.append([tempy, tempx])
                elif tiddup[tempy][tempx] == 'D':
                    result = time
                    return

    if not nextWq and not nextHq:  # 더 갈 곳이 없으면
        return
    bfs(nextWq, nextHq, time + 1)


bfs(waterq, hedgehogq, 1)
if result:
    print(result)
else:
    print('KAKTUS')
