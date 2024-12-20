a:int = int(input())
arr = []
i = 0
for i in range(a):
    arr.append(int(input()))
    i+=1

arr2 = sorted(arr)
while arr2:
    print(arr2[0])
    arr2.pop(0)
