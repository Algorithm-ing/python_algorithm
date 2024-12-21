"""
숫자 정렬
"""
N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)
for number in sorted(numbers):
    print(number)