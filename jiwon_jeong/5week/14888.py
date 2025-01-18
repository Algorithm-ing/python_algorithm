# 백준 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
operators_cnt = list(map(int, sys.stdin.readline().split())) # +, -, x, /

def sol(N, A, operators_cnt):
    operators = []
    for i, cnt in enumerate(operators_cnt):
        operators.extend(["+", "-", "*", "/"][i] * cnt)

    max_result = -1
    min_result = float('inf')

    for perm in permutations(operators):
        
        result = A[0]
        for i in range(1, N):
            if perm[i -1] == '+':
                result += A[i]
            elif perm[i - 1] == '-':
                result -= A[i]
            elif perm[i - 1] == '*':
                result *= A[i]
            elif perm[i - 1] == '/':
                if result < 0:
                    result = -(-result // A[i])
                else:
                    result //= A[i]
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    return max_result, min_result
print(*sol(N=N, A=A, operators_cnt=operators_cnt), sep='\n')