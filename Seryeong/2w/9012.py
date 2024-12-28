# 괄호
T = int(input())

for _ in range(T):
    line = list(input())
    stack = []
    for i in line:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) > 0:
                if stack[len(stack) - 1] == ')':
                    stack.append(')')
                else:
                    stack.pop()
            else:
                stack.append(')')
    if len(stack) > 0:
        print('NO')
    else:
        print('YES')
