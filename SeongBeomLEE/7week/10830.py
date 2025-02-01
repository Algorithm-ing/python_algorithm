import sys
input = sys.stdin.readline
N, B = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

def mul(A, B):
    N = len(A)
    M = len(A[0])
    K = len(B[0])
    C = [[0 for _ in range(K)] for _ in range(N)]
    for row in range(N):
        for col in range(K):
            e = 0
            for i in range(M):
                e += A[row][i] * B[i][col]
            C[row][col] = e % 1000
    return C

def sol(A, B):
    if B == 1:
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] %= 1000
        return A
    tmp = sol(A, B // 2)
    if B % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), A)
    
result = sol(array, B)
for i in result:
    print(*i)