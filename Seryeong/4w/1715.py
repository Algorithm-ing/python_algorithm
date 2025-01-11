# 카드 정렬하기 - 힙

import sys
import heapq
N = int(sys.stdin.readline())

if N == 1:  # 카드가 한 장일 경우 비교할 필요 없음
    print(0)
else:
    cards = []
    # 카드 추가
    for _ in range(N):
        card = int(sys.stdin.readline())
        cards.append(card)

    heapq.heapify(cards)  # 정렬

    result = 0
    while len(cards) >= 2:
        bundle = heapq.heappop(cards) + heapq.heappop(cards)  # 비교 횟수 추가
        result += bundle
        heapq.heappush(cards, bundle)

    print(result)
