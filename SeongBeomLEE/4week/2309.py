import sys
input = sys.stdin.readline
numbers = []
for _ in range(9):
    number = int(input())
    numbers.append(number)

answers = [[number] for number in numbers]
while True:
    answer = answers.pop()
    if len(answer) == 7 and sum(answer) == 100:
        break
    if len(answer) > 7 or sum(answer) > 100:
        continue
    for number in numbers:
        if number not in answer:
            answers.append(answer[:] + [number])

for i in sorted(answer):
    print(i)