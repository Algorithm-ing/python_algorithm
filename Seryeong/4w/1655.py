# 가운데를 말해요 - 힙
import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []
min_heap = []
mid = 0

for _ in range(N):
    input = int(sys.stdin.readline())
    # 중간값보다 입력값이 크면
    if mid < input:
        # 오른쪽(최소 힙으로)
        heapq.heappush(min_heap, input)
    # 중간값보다 입력값이 작으면
    else:
        # 왼쪽(최대 힙으로)
        heapq.heappush(max_heap, -input)

    # 최대 힙이 2개 더 커지면
    if len(max_heap) > len(min_heap)+1:
        # 최소 힙으로 하나 옮기기
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    # 최소 힙이 커지면
    elif len(min_heap) > len(max_heap):
        # 최대 힙으로 하나 옮기기
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    mid = -max_heap[0]
    print(mid)
