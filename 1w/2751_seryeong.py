import sys

n = int(input())
input = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(input):
    print(i)
