results = set()

def solution(cards:list[int], n:int, k:int, cnt:int, result:str, visit:list):
    if cnt == k:
        results.add(result)
        return
    for index in range(n):
        if visit[index]:
            continue
        visit[index] = True
        solution(cards, n, k, cnt + 1, result + str(cards[index]), visit)
        visit[index] = False

N = int(input())
K = int(input())
cards = []
for _ in range(N):
    card = int(input())
    cards.append(card)
visit = [False for _ in range(N)]
solution(cards, N, K, 0, "", visit)
print(len(results))