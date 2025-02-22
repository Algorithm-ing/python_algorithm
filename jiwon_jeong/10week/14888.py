# 백준 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
################################# 완전 탐색 ###########################
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
operator_cnt = list(map(int, sys.stdin.readline().split()))

def sol(N, A, operator_cnt):
    operators = []
    for i, cnt in enumerate(operator_cnt):
        operators.extend(['+', '-', '*', '/'][i] * cnt)
    
    max_result = -float('inf')
    min_result = float('inf')
    
    for perm in permutations(operators):
        result = A[0]
        
        for i in range(1, N):
            if perm[i - 1] == '+':
                result += A[i]
            elif perm[i - 1] == '-':
                result -= A[i]
            elif perm[i - 1] == '*':
                result *= A[i]
            else:
                if result < 0:
                    result = -(-result // A[i])
                else:
                    result //= A[i]
        max_result, min_result = max(max_result, result), min(min_result, result)
    
    return max_result, min_result
print(*sol(N=N, A=A, operator_cnt=operator_cnt), sep='\n')
################################# 완전 탐색 ###########################

################################# 백트래킹 ###########################
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
operator_cnt = list(map(int, sys.stdin.readline().split()))

max_result, min_result = -float('inf'), float('inf')

def backtrack(index, current_result, plus, minus, mul, div):
    global max_result, min_result
    
    if index == N:
        max_result = max(current_result, max_result)
        min_result = min(current_result, min_result)
        return
    
    if plus > 0:
        backtrack(index + 1, current_result + A[index], plus - 1, minus, mul, div)
    if minus > 0:
        backtrack(index + 1, current_result - A[index], plus, minus - 1, mul, div)
    if mul > 0:
        backtrack(index + 1, current_result * A[index], plus, minus, mul - 1, div)
    if div > 0:
        if current_result < 0:
            backtrack(index + 1, -(-current_result // A[index]), plus, minus, mul, div - 1)
        else:
            backtrack(index + 1, current_result // A[index], plus, minus, mul, div - 1)

backtrack(1, A[0], *operator_cnt)
print(max_result, min_result, sep='\n')
################################# 백트래킹 ###########################