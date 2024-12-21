import sys
N = int(sys.stdin.readline().strip())
columns = [False] * N
diagonals1 = [False] * (2 * N - 1) # 위에서 아래로 내려가는 방향의 대각선
diagonals2 = [False] * (2 * N - 1)


def solve_n_queens(n, row, columns, diagonals1, diagonals2):
    if row == n:
        return 1
    cnt = 0
    for col in range(n):
        if columns[col] or diagonals1[row + col] or diagonals2[row - col - n + 1]:
            continue
        
        columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = True
        cnt += solve_n_queens(n, row + 1, columns, diagonals1, diagonals2)
        columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = False
        
    return cnt

result = solve_n_queens(n=N, row=0, columns=columns, diagonals1=diagonals1, diagonals2=diagonals2)
print(result)