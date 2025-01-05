import sys
import heapq
input = sys.stdin.readline
N = int(input())
max_heap = [] # 중앙값 이하를 저장 (최대 힙)
min_heap = [] # 중앙값 이상을 저장 (최소 힙)
for _ in range(N):
    number = int(input())

    # 최대 힙에 새 값 추가 (음수로 저장하여 최대 힙 구현)
    if not max_heap or number <= -max_heap[0]:
        heapq.heappush(max_heap, -number)
    else:
        heapq.heappush(min_heap, number)

    # 힙의 크기를 조정 (최대 힙 크기가 최소 힙 크기보다 많아야 함)
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    median = -max_heap[0]
    print(median)