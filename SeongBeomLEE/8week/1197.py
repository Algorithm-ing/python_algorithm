"""
크루스칼 알고리즘을 활용한 풀이
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A - 1, B - 1, C))
edges = sorted(edges, key=lambda edge: edge[2])
parent = [i for i in range(V)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
cnt = 0
for A, B, C in edges:
    if not same_parent(A, B):
        union_parent(A, B)
        answer += C
        cnt += 1
    if cnt == V - 1:
        break

print(answer)