import sys
input = sys.stdin.readline
N, K = map(int, input().split())
numbers = input().rstrip()
stack = []
cnt = 0
for index in range(N):
    while cnt < K and stack and stack[-1] < numbers[index]:
        stack.pop()
        cnt += 1
    stack.append(numbers[index])
print("".join(stack[:N - K]))