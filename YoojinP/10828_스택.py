import sys

N = int(input())

stack = []
answer = []
    
for i in range(N):
    r = sys.stdin.readline().split(" ")  
    if r[0] == "push" :  # push      
        stack.append(r[1][:-1])
    elif r[0][:-1] == "top":
        if len(stack)==0:
            answer.append(-1)
            continue
        answer.append(stack[-1])
    elif r[0][:-1] == "size":
        answer.append(len(stack))
    elif r[0][:-1] == "empty":
        e = 1 if len(stack)==0 else 0
        answer.append(e)
    else:  # pop
        if len(stack)==0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
            stack = stack[:-1]
        
for a in answer:
    print(a)