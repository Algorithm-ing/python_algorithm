import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
S = list(map(int, input().split()))
animals = []
for _ in range(N):
    animals.append(list(map(int, input().split())))

S = sorted(S)
answer = 0
for a, b in animals:
    start = 0
    end = M - 1
    left = a + b - L
    right = a - b + L
    while start <= end:
        mid = (start + end) // 2
        if left <= S[mid] <= right:
            answer += 1
            break
        if S[mid] < left:
            start = mid + 1
        else:
            end = mid - 1

print(answer)