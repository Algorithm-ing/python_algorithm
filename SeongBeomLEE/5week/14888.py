import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_answer = -9876543210
min_answer = 9876543210

def dfs(n, answer):
    global max_answer, min_answer
    if n == N - 1:
        max_answer = max(max_answer, answer)
        min_answer = min(min_answer, answer)
        return

    # 덧셈
    if operators[0] != 0:
        operators[0] -= 1
        dfs(n + 1, answer + array[n + 1])
        operators[0] += 1

    # 뺄셈
    if operators[1] != 0:
        operators[1] -= 1
        dfs(n + 1, answer - array[n + 1])
        operators[1] += 1

    # 곱셈
    if operators[2] != 0:
        operators[2] -= 1
        dfs(n + 1, answer * array[n + 1])
        operators[2] += 1

    # 나눗셈
    if operators[3] != 0:
        operators[3] -= 1
        dfs(n + 1, int(answer / array[n + 1]))
        operators[3] += 1

dfs(0, array[0])
print(max_answer)
print(min_answer)