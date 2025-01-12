# 백준 1655. 가운데를 말해요
# https://www.acmicpc.net/problem/1655
import sys
from heapq import heappush, heappop
N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]
def sol(nums):
    max_heap = []
    min_heap = []
    result = []
    for num in nums: 
        if not max_heap or num <= -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        
        result.append(-max_heap[0])
    return '\n'.join(map(str, result))
print(sol(nums=nums))
        