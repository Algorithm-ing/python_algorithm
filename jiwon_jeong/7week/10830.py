# 백준 10830. 행렬 제곱
# https://www.acmicpc.net/problem/10830
import sys
N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def matrix_multiply(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def sol(A, B, N):
    
    # 1. base case
    if B == 1:
        return[[A[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    # 2. 재귀 호출
    half = sol(A, B // 2, N)
    
    half = matrix_multiply(half, half, N)

    # 3. 데이터 통합
    if B % 2 == 0:
        return half
    else:
        return matrix_multiply(half, A, N)    

result = sol(A=A, B=B, N=N)
for row in result:
    print(*row)
    

