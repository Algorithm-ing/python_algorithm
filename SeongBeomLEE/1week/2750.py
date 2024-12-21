"""
재귀를 활용한 숫자 정렬
Recursive Insertion Sort
"""
import sys
# 재귀 함수를 1,000번 이상 실행 시키기 위함
sys.setrecursionlimit(987654321)

def insert(numbers:list[int], index:int):
    if len(numbers) <= index or numbers[index - 1] <= numbers[index]:
        return
    # 현재 위치의 숫자 보다 이전 위치의 숫자가 더 크기 때문에 순서를 변경
    numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]
    insert(numbers, index + 1)

def rec_sort(numbers:list[int], n:int):
    if len(numbers) <= 1 or n <= 1:
        return
    # 마지막 순서 정렬
    insert(numbers, n - 1)
    # 이전 순서 정렬 시작
    rec_sort(numbers, n - 1)

N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)
rec_sort(numbers, N)
for number in numbers:
    print(number)