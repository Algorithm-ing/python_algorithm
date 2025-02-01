# 백준 2630. 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys
N = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt0, cnt1 = 0, 0
def sol(matrix, x, y, size):
    global cnt0, cnt1
    is_same = True
    first_val = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_val:
                 is_same = False
                 break
        if not is_same:
            break
    if is_same:
        if first_val == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    else:
        new_size = size // 2
        for i in range(2):
            for j in range(2):
                sol(matrix, x + i * new_size, y + j * new_size, new_size)

sol(matrix, 0, 0, N)
print(cnt0, cnt1, sep='\n')