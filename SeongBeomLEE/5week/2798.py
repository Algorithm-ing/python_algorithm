import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            if i != j and j != k and i != k:
                now = cards[i] + cards[j] + cards[k]
                if now <= M:
                    answer = max(answer, now)
print(answer)