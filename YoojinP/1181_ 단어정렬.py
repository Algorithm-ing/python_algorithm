#1181_ 단어정렬

import sys

N = int(input())
arr = []
for _ in range(N):
    string = sys.stdin.readline()[:-1]
    if string in arr:
        continue
    arr.append(string)

temp = sorted(arr, key= lambda x: (len(x), x))
for t in temp:
    print(t)
