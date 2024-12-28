# 단어 정렬
import sys

n = int(input())
input = list(set([input() for _ in range(n)]))

input.sort(key=lambda x: (len(x), x))

for i in input:
    print(i)
