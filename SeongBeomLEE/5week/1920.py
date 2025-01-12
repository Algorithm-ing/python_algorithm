import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

array.sort()
def bibary_serch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: 
            return 1
        elif array[mid] < target: 
            start = mid + 1
        else: 
            end = mid - 1
    return 0

for target in targets:
    print(bibary_serch(array, target))