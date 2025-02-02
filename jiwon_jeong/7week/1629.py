# 백준 1629. 곱셈
# https://www.acmicpc.net/problem/1629
import sys
A, B, C = map(int, sys.stdin.readline().split())
def sol(a, b, c):
    # 1. base case
    if b == 0:
        return 1
    
    # 2. 재귀 호출
    half = sol(a, b // 2, c)
    
    half = half * half % c
    if b % 2 !=0:
        half = half * a % c
    
    return half
print(sol(a=A, b=B, c=C))