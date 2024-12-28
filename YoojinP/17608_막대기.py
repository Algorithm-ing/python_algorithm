import sys 

N =int(input())
stack = []

for i in range(N):
    stack.append(sys.stdin.readline()[:-1])
    
max_num = 0
count = 0
for s in stack[::-1]:
    s = int(s)
    if max_num < s:
        max_num = s
        count +=1
print(count)