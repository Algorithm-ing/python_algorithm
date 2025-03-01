import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
maps = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    maps[A].append(B)

answers = [-1] * (N + 1)
answers[X] = -2
nodes = deque([[X, 1]])
while nodes:
    A, cnt = nodes.popleft()
    for B in maps[A]:
        if answers[B] == -1:
            answers[B] = cnt
            nodes.append([B, cnt + 1])

cnt = 0
for index, k in enumerate(answers):
    if k == K:
        cnt += 1
        print(index)
if cnt == 0:
    print(-1)