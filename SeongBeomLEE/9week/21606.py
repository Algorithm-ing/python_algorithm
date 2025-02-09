import sys
input = sys.stdin.readline
N = int(input())
status = list(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

visited = [False] * N
answer = 0
for root in range(N):
    # 실내 -> 실내 가는 경우
    if status[root] == "1":
        for node in G[root]:
            if status[node] == "1":
                answer += 1
    # 실내 -> 실외... -> 실내 가는 경우
    else:
        if not visited[root]:
            nodes = [root]
            visited[root] = True
            cnt = 0
            while nodes:
                root = nodes.pop()
                for node in G[root]:
                    if status[node] == "1":
                        cnt += 1
                    else:
                        if not visited[node]:
                            visited[node] = True
                            nodes.append(node)
            answer += cnt * (cnt - 1)
print(answer)