import sys
input = sys.stdin.readline
N, K = map(int, input().split())
levels = []
for _ in range(N):
    levels.append(int(input()))

start = 1
end = min(levels) + K
T = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for level in levels:
        if level < mid:
            total += mid - level
    if total <= K:
        T = max(T, mid)
        start = mid + 1
    else:
        end = mid - 1

print(T)