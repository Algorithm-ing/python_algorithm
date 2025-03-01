"""
- 고슴 도치 이동
-- 비어있는 곳만 이동
- 물 이동
-- 고슴 도치가 있는 곳, 비어있는 곳 모두 이동동
"""

import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
maps = []
min_cost_maps = [[0] * C for _ in range(R)]
for _ in range(R):
    maps.append(list(input()))

D_loc = []
S_loc = []
W_loc = []
for row in range(R):
    for col in range(C):
        if maps[row][col] == "D":
            D_loc.append([row, col])
        if maps[row][col] == "S":
            S_loc.append([row, col])
        if maps[row][col] == "*":
            W_loc.append([row, col])

answer = "KAKTUS"
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
moves = deque()
for s_loc in S_loc:
    moves.append(s_loc)
for w_loc in W_loc:
    moves.append(w_loc)

while moves:
    row, col = moves.popleft()
    if maps[D_loc[0][0]][D_loc[0][1]] == "S":
        answer = min_cost_maps[D_loc[0][0]][D_loc[0][1]]
        break
    for dr, dc in zip(drs, dcs):
        r, c = row + dr, col + dc
        if 0 > r or r >= R or 0 > c or c >= C:
            continue
        if maps[row][col] == "S" and (maps[r][c] == "." or maps[r][c] == "D"):
            maps[r][c] = "S"
            min_cost_maps[r][c] = min_cost_maps[row][col] + 1
            moves.append([r, c])
        if maps[row][col] == "*" and (maps[r][c] == "." or maps[r][c] == "S"):
            maps[r][c] = "*"
            moves.append([r, c])
print(answer)
