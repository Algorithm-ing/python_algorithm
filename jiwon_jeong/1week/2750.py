# 백준 2750번. 수 정렬하기
# https://www.acmicpc.net/problem/2750
import sys
N =int(sys.stdin.readline().strip())
num = sorted(list(int(sys.stdin.readline().strip()) for _ in range(N)))
print('\n'.join(map(str, num)))
