import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
maps = [[0 for _ in range(N)] for _ in range(N)] # -1 - 뱀 / 0 - 땅 / 1 - 사과
for _ in range(K):
    row, col = map(int, input().split())
    maps[row - 1][col - 1] = 1

L = int(input())
inputs = deque([])
for _ in range(L):
    inputs.append(input().split())

answer = 0
row, col = 0, 0
snake_posions = deque([])
pos = 0 # 오 - 0 / 왼 - 1 / 위 - 2 / 아 - 3
while True:
    if inputs:
        if answer == int(inputs[0][0]):
            if pos == 0:
                pos = 3 if inputs[0][1] == "D" else 2
            elif pos == 1:
                pos = 2 if inputs[0][1] == "D" else 3
            elif pos == 2:
                pos = 0 if inputs[0][1] == "D" else 1
            elif pos == 3:
                pos = 1 if inputs[0][1] == "D" else 0
            inputs.popleft()
    
    if maps[row][col] == 1:
        maps[row][col] = -1
        snake_posions.append([row, col])
    elif maps[row][col] == 0:
        maps[row][col] = -1
        if snake_posions:
            snake_posion = snake_posions.popleft()
            maps[snake_posion[0]][snake_posion[1]] = 0
        snake_posions.append([row, col])
    else:
        break

    answer += 1
    if pos == 0:
        col += 1
    elif pos == 1:
        col -= 1
    elif pos == 2:
        row -= 1
    elif pos == 3:
        row += 1

    if col == N or col < 0 or row == N or row < 0:
        break

print(answer)