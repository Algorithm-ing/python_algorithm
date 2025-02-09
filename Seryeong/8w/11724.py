# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
input = []
for _ in range(M):
    input.append(list(map(int, sys.stdin.readline().split())))

# 연결 리스트 만들기
graph = [[] for _ in range(N+1)]
for i in input:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in input:
    i = sorted(i)

# DFS
el = 0
visited = [0]*(N+1)


def DFS(start):
    global el, visited
    visited[start] += 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)


# 블로그 코드 참고 =====================================
for i in range(1, len(visited)):
    if not visited[i]:
        # 🚨 정점이 없는 경우는 굳이 DFS를 하면서 시간을 낭비할 필요가 없음
        if not graph[i]:
            el += 1
            visited[i] = 1
        else:
            DFS(i)
            # 탐색이 끝날 때마다 실행하고 싶을 때 재귀함수 안에 넣으면 복잡함
            # 🚨 재귀함수 바깥에서 세기
            el += 1

print(el)
