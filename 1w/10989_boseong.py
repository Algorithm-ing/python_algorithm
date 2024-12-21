import sys
a: int = int(sys.stdin.readline())
arr = [0] * 10000
for _ in range(a):
    val = int(sys.stdin.readline())
    arr[val - 1] = arr[val - 1] + 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)