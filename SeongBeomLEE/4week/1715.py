import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    number = int(input())
    heapq.heappush(heap, number)

answer = 0
while len(heap) != 1:
    number1 = heapq.heappop(heap)
    number2 = heapq.heappop(heap)
    number = number1 + number2
    answer += number
    heapq.heappush(heap, number)

print(answer)
