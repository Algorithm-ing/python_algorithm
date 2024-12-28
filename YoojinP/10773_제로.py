k = int(input())

stack = []
for i in range(k):
    num = int(input())
    if num == 0:
        stack= stack[:-1]
    else:
        stack.append(num)
        
total = sum(stack)
print(total)