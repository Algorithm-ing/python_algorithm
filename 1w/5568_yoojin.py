# 1. permutation
# 2. 알고리즘

from itertools import combinations, permutations

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    c = input()
    arr.append(c)
    
combi = list(permutations(arr, k))
set_combi = set()
for c in combi:
    string = ""
    for c_i in c:
        string += c_i
    set_combi.add(string)

print(len(set_combi))
