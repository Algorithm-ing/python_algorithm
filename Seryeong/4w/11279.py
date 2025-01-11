# 힙 - 최대 힙
# 최대 힙 넣기: heapq.heappush(heap, -input)
# 최대 힙 빼기: -heapq.heappop(heap)

import sys
import heapq
input = int(sys.stdin.readline())

heap = []
for _ in range(input):
    input = int(sys.stdin.readline())
    if input == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])  # print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-input, input))  # heapq.heappush(heap, -input)
