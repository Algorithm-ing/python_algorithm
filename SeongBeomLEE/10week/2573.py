import sys
from collections import deque
def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    seas = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우
    answer = 0

    while True:
        ice_cnt = 0
        answer += 1
        for row in range(N):
            for col in range(M):
                if maps[row][col] != 0:
                    ice_cnt += 1
                    for _row, _col in moves:
                        if maps[row + _row][col + _col] == 0:
                            seas[row][col] += 1

        if ice_cnt == 0:
            answer = 0
            break

        ice_cnt = 0
        checks = []
        for row in range(N):
            for col in range(M):
                maps[row][col] = max(0, maps[row][col] - seas[row][col])
                seas[row][col] = 0
                visited[row][col] = 0
                if maps[row][col] >= 1:
                    ice_cnt += 1 
                    checks = [[row, col]]
        
        if ice_cnt == 0:
            answer = 0
            break

        visit_ice_cnt = 1
        visited[checks[0][0]][checks[0][1]] = 1
        checks = deque(checks)
        while checks:
            row, col = checks.popleft()
            for _row, _col in moves:
                if row + _row < 0 or row + _row >= N or col + _col < 0 or col + _col >= M:
                    continue
                if maps[row + _row][col + _col] > 0 and visited[row + _row][col + _col] != 1:
                    visited[row + _row][col + _col] = 1
                    visit_ice_cnt += 1
                    checks.append([row + _row, col + _col])
        
        if visit_ice_cnt != ice_cnt:
            break

    print(answer)

solution()