import sys
input = sys.stdin.readline
N = int(input())
An = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_answer = -987654321987654321
min_answer = 987654321987654321
answers = [[An[0], 0, operators[:]]]
while answers:
    answer, index, operators = answers.pop()
    if index == N - 1:
        max_answer = max(max_answer, answer)
        min_answer = min(min_answer, answer)
        continue
    for operator_index in range(len(operators)):
        if operator_index == 0 and operators[operator_index] != 0:
            operators[operator_index] -= 1
            answers.append([answer + An[index + 1], index + 1, operators[:]])
            operators[operator_index] += 1
        elif operator_index == 1 and operators[operator_index] != 0:
            operators[operator_index] -= 1
            answers.append([answer - An[index + 1], index + 1, operators[:]])
            operators[operator_index] += 1
        elif operator_index == 2 and operators[operator_index] != 0:
            operators[operator_index] -= 1
            answers.append([answer * An[index + 1], index + 1, operators[:]])
            operators[operator_index] += 1
        elif operator_index == 3 and operators[operator_index] != 0:
            operators[operator_index] -= 1
            answers.append([answer // An[index + 1] if answer >= 0 else -(-answer // An[index + 1]), index + 1, operators[:]])
            operators[operator_index] += 1

print(max_answer)
print(min_answer)

