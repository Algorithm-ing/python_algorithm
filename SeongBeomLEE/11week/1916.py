# 다익스트라 알고리즘을 활용한 풀이
import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, cost = map(int, input().split())
    bus[A].append([B, cost])
start, end = map(int, input().split())
moves = []
answers = [9876543210] * (N + 1)
heapq.heappush(moves, (0, start))
answers[start] = 0
while moves:
    total_cost, A = heapq.heappop(moves)
    if answers[A] < total_cost:
        continue
    for B, cost in bus[A]:
        if cost + total_cost < answers[B]:
            answers[B] = cost + total_cost
            heapq.heappush(moves, (cost + total_cost, B))
print(answers[end])