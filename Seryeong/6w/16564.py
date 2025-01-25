# 히오스 프로게이머 - 이분탐색
import sys

N, K = map(int, sys.stdin.readline().split())
levels = [int(sys.stdin.readline()) for _ in range(N)]

start = 0
end = max(levels) + K  # K를 더할 수 있음
maxNum = 0  # 최대 팀 목표레벨

while start <= end:
    mid = (start + end) // 2

    need = 0
    for level in levels:
        if level < mid:
            need += mid - level

    if need > K:  # 올릴 수 있는 레벨 총합을 초과하면
        end = mid - 1
    else:
        maxNum = max(maxNum, mid)
        start = mid + 1

print(maxNum)
