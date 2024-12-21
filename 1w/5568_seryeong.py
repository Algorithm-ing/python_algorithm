import itertools

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

result = set()
for i in list(itertools.permutations(cards, k)):
    result.add(''.join(i))

print(len(result))
