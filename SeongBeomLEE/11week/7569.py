# BFS 를 사용해서 최소 탐색 횟수를 먼저 구한다.

import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
drs, dcs, dhs = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

moves = deque()
for high in range(H):
    for row in range(N):
        for col in range(M):
            if tomatos[high][row][col] == 1:
                moves.append([high, row, col])

while moves:
    high, row, col = moves.popleft()
    for dr, dc, dh in zip(drs, dcs, dhs):
        r, c, h = row + dr, col + dc, high + dh
        if 0 <= r and r < N and 0 <= c and c < M and 0 <= h and h < H and tomatos[h][r][c] == 0:
            tomatos[h][r][c] = tomatos[high][row][col] + 1
            moves.append([h, r, c])

check = True
answer = 0
for high in range(H):
    for row in range(N):
        for col in range(M):
            if tomatos[high][row][col] == 0:
                check = False
            answer = max(answer, tomatos[high][row][col])

if check:
    print(answer - 1)
else:
    print(-1)