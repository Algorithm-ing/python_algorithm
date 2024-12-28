import sys
N = int(input())

stack = []
for _ in range(N):
    num = int(sys.stdin.readline())  # 문자열로 비교하면 안됨
    while stack and stack[-1] < num:
        stack.pop()
    if not stack or stack[-1] != num:
        stack.append(num)

print(len(stack))
