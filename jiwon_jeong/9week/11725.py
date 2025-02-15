# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# ######################### DFS ######################
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    def dfs(node, tree, parents):
        for child in tree[node]:
            if parents[child] == 0:
                parents[child] = node
                dfs(child, tree, parents)
    parents[1] = -1
    dfs(1, tree, parents)
    print(*parents[2:], sep='\n')
main()
######################## DFS ######################

######################### BFS ######################
import sys
from collections import defaultdict, deque
def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    def bfs(node, tree, parents):
        q = deque()
        q.append(node)
        parents[node] = -1
        while q:
            cur_node = q.popleft()
            for child in tree[cur_node]:
                if parents[child] == 0:
                    parents[child] = cur_node
                    q.append(child)
        return parents
    print(*bfs(1, tree, parents)[2:], sep='\n')
main()
######################### BFS ######################