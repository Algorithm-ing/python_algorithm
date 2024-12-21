# 백준 9663. N-Queen
# https://www.acmicpc.net/problem/9663


# ####################### 시간 초과 ############################
# import sys

# def check(row, col, queens):
#     """
#     현재 퀸의 (row, col)이 기존 퀸들과 충돌하지 않는지 검사
#     queens: 각 행에 놓인 퀸의 열 정보를 저장
#     """
#     for r in range(row):
#         c = queens[r]
#         if c == col or abs(r - row) == abs(c - col):
#             return False
#     return True

# def solve_n_queens(n, row, queens):
#     """
#     n: 체스판 크기
#     row: 현재 처리 중인 행
#     queens: 현재까지 놓인 퀸의 열 위치를 저장
#     """
#     if row == n:
#         return 1
#     cnt = 0
#     for col in range(n): # 현재 행에서 모든 열 탐색
#         if check(row, col, queens):
#             queens[row] = col
#             cnt += solve_n_queens(n, row + 1, queens) # 다음 행 탐색
#             queens[row] = -1
#     return cnt


# N = int(sys.stdin.readline().strip())
# queens = [-1] * N
# result = solve_n_queens(N, 0, queens)
# print(result)
####################### 시간 초과 ############################

import sys

def solve_n_queens(n, row, columns, diagonals1, diagonals2):
    """
    n: 체스판 크기
    row: 현재 처리 중인 행
    columns: 열 사용 여부 추적
    diagonals1: 좌측 대각선 사용 여부 추적 (row + col)
    diagonals2: 우측 대각선 사용 여부 추적 (row - col)
    """
    if row == n:  # 모든 퀸을 배치한 경우
        return 1

    count = 0
    for col in range(n):  # 현재 행에서 모든 열 탐색
        if columns[col] or diagonals1[row + col] or diagonals2[row - col + n - 1]:
            continue  # 현재 열 또는 대각선이 점유되었으면 스킵

        # 상태 업데이트
        columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = True
        count += solve_n_queens(n, row + 1, columns, diagonals1, diagonals2)
        # 상태 복원 (백트래킹)
        columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = False

    return count


# 입력 및 실행
N = int(sys.stdin.readline().strip())

# 열과 대각선 상태 추적 배열
columns = [False] * N
diagonals1 = [False] * (2 * N - 1)  # 좌측 대각선
diagonals2 = [False] * (2 * N - 1)  # 우측 대각선

result = solve_n_queens(N, 0, columns, diagonals1, diagonals2)
print(result)




