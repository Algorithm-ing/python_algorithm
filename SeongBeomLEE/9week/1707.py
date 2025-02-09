import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
    answer = True
    visited = [0] * V # 0 - 미방분 / 1 - red / 2 - blue
    for node in range(V):
        if visited[node] == 0:
            nodes = [node]
            visited[node] = 1
            while nodes:
                root = nodes.pop()
                for node in G[root]:
                    if visited[node] == 0:
                        visited[node] = 2 if visited[root] == 1 else 1
                        nodes.append(node)
                    else:
                        if visited[root] == visited[node]:
                            answer = False
                            break
                if not answer:
                    break
        if not answer:
            break
    print("YES" if answer else "NO")