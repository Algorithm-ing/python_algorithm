strings = input()
answer = 0
stack = []
numbers = []

for idx, c in enumerate(strings):
    if c == '(' or c == '[':
        stack.append((c, idx))
    elif c == ')' or c ==']':
        if not stack:
            stack.append((c, idx))
            break
        if c == ')':
            if stack[-1][0] == '(':
                if idx - stack[-1][1] == 1:
                    numbers.append((2, stack[-1][1]))
                    stack.pop()
                else:
                    new_numbers = []
                    total = 0
                    for number in numbers:
                        if stack[-1][1] < number[1]:
                            total += number[0]
                        else:
                            new_numbers.append(number)
                    numbers = new_numbers
                    total = 2 * total
                    numbers.append((total, stack[-1][1]))
                    stack.pop()
            else:
                stack.append((c, idx))
                break
        elif c == ']':
            if stack[-1][0] == '[':
                if idx - stack[-1][1] == 1:
                    numbers.append((3, stack[-1][1]))
                    stack.pop()
                else:
                    new_numbers = []
                    total = 0
                    for number in numbers:
                        if stack[-1][1] < number[1]:
                            total += number[0]
                        else:
                            new_numbers.append(number)
                    numbers = new_numbers
                    total = 3 * total
                    numbers.append((total, stack[-1][1]))
                    stack.pop()
            else:
                stack.append((c, idx))
                break

if stack:
    answer = 0
else:
    for number in numbers:
        answer += number[0]

print(answer)
