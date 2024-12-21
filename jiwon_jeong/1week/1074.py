# 백준 1074. Z
# https://www.acmicpc.net/problem/1074
import sys
N, r, c = map(int, sys.stdin.readline().split())

def z_order(n, r, c):
    if n == 0:
        return 0
    size = 2 ** (n - 1)
    half = size ** 2
    if r < size and c < size: # 1사분면
        return z_order(n - 1, r, c)
    elif r < size and c >= size: # 2사분면
        return half + z_order(n - 1, r, c - size)
    elif r >= size and c < size: # 3사분면
        return 2 * half + z_order(n - 1, r - size, c)
    else: # 4사분면
        return 3 * half + z_order(n - 1, r - size, c - size)
    
print(z_order(n=N, r=r, c=c))