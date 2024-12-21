#2751_수 정렬하기2
import sys

#input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
   
for a in sorted(arr):
    print(a)