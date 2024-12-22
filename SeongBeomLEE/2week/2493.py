import sys
input = sys.stdin.readline
N = int(input())

top_array = list(map(int, input().rstrip().split(" ")))
stack = []
answer = [0] * N

for index in range(N):
    while stack:
        if stack[-1][1] > top_array[index]:
            answer[index] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    if not stack:
        answer[index] = 0
    stack.append([index, top_array[index]])

print(" ".join(list(map(str, answer))))