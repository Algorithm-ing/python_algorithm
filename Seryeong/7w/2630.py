# 색종이 만들기 - 분할정복

import sys

N = int(sys.stdin.readline())
colors = [sys.stdin.readline().split() for _ in range(N)]
blue, white = [0, 0]


def check_color(x, y, size):
    flag = False
    current_color = colors[y][x]
    for plus_y in range(size):
        for plus_x in range(size):
            if current_color != colors[y + plus_y][x + plus_x]:  # 색이 하나라도 다르면
                flag = True
                break
        if flag:
            break

    if flag:
        next_size = size // 2
        check_color(x, y, next_size)
        check_color(x + next_size, y, next_size)
        check_color(x, y + next_size, next_size)
        check_color(x + next_size, y + next_size, next_size)
    else:
        global blue, white
        if current_color == '1':
            blue += 1
        else:
            white += 1
        return


check_color(0, 0, N)
print(white)
print(blue)
