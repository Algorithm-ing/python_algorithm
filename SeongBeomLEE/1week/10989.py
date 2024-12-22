import sys

N = int(input())
numbers = [0 for _ in range(10001)]
for _ in range(N):
    number = int(sys.stdin.readline())
    numbers[number] += 1
for number in range(len(numbers)):
    if numbers[number] > 0:
        for _ in range(numbers[number]):
            print(number)