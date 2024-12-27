# 백준 2812. 크게 만들기
# https://www.acmicpc.net/problem/2812
import sys
N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()
def sol(N, K, num):
    stack = []
    i = 0
    for n in num:
        while stack and i < K and stack[-1] < n:
            stack.pop()
            i += 1
        stack.append(n)
    return ''.join(stack[:N-K])
print(sol(N=N, K=K, num=num))