import sys
input = sys.stdin.readline
N = int(input())
G = {}
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if A not in G:
        G[A] = []
    if B not in G:
        G[B] = []
    G[A].append(B)
    G[B].append(A)

V = [-1] * N
nodes = [0]
V[0] = 1
while nodes:
    root = nodes.pop()
    if root in G:
        for node in G[root]:
            if V[node] == -1:
                V[node] = root + 1
                nodes.append(node)

for i in V[1:]:
    print(i)