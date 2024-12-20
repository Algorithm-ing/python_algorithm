from itertools import permutations

n = int(input())
k = int(input())

num = []

for _ in range(n):
    num.append(input())

res = set()

for i in permutations(num, k):
    res.add(''.join(i))

print(len(res))