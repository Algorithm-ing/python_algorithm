import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Gh = [[] for _ in range(N)]
Gm = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    Gh[B - 1].append(A - 1)
    Gm[A - 1].append(B - 1)

def solution(G):
    answers = [0] * N
    for i in range(N):
        visited = [False] * N
        nodes = [i]
        while nodes:
            node = nodes.pop()
            for next_node in G[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    answers[next_node] += 1
                    nodes.append(next_node)

    answer = 0
    for i in answers:
        if N // 2 < i:
            answer += 1
    
    return answer

answer = solution(Gh) + solution(Gm)
print(answer)