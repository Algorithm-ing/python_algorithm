# 스택
N = int(input())
input = [input() for _ in range(N)]

stack = []
for line in input:
    if line.startswith('push'):
        stack.append(line.split()[1])
    elif line.startswith('pop'):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif line.startswith('size'):
        print(len(stack))
    elif line.startswith('empty'):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif line.startswith('top'):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
