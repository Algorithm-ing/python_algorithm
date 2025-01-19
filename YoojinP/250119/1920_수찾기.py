import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rsplit()))

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rsplit()))

data.sort()
ans = []

def find_num(target, data):
    start = 0 
    end = len(data)-1
    
    while start <= end:
        mid = (start + end)//2
        #print(f"start:{start}, end:{end}, mid:{mid} => data[mid]:{data[mid]}, target:{target}")

        if data[mid] == target :    
            return 1
        elif data[mid] < target:
            start = mid +1
        else:
            end = mid -1

    return 0

for num in nums:
    t = find_num(num, data)
    ans.append(t)

for a in ans:
    print(a)