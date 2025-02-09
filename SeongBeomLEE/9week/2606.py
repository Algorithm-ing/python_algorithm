import sys
input = sys.stdin.readline
N = int(input())
E = int(input())
G = [[0] * N for _ in range(N)]
for _ in range(E):
    A, B = map(int, input().split())
    G[A - 1][B - 1] = 1
    G[B - 1][A - 1] = 1
V = [False] * N
nodes = [0]
V[0] = True
while nodes:
    root = nodes.pop()
    for node in range(N):
        if not V[node] and G[root][node] == 1:
            V[node] = True
            nodes.append(node)
answer = 0
V[0] = False
for i in V:
    if i:
        answer += 1
print(answer)