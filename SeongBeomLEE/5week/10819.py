import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
combinations = [[i] for i in range(N)]
answer = 0
while combinations:
    combination = combinations.pop()
    if len(combination) == N:
        now = 0
        for i in range(N - 1):
            now += abs(array[combination[i]] - array[combination[i + 1]])
        answer = max(now, answer)
        continue
    for i in range(N):
        if i not in combination:
            combinations.append(combination[:] + [i])
print(answer)


