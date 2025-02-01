"""
10 ^ 11 % 12 = (10 ^ 5 x 10 ^ 5 x 10) % 12 = (10 ^ 5 % 12) x (10 ^ 5 % 12) x (10 % 12) % 12

"""
import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def sol(a, b, c):
    if b == 1:
        return a % c
    num = sol(a, b // 2, c)
    if b % 2 == 0:
        return (num * num) % c
    else:
        return (num * num * a) % c

print(sol(A, B, C))