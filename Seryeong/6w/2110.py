# 공유기 설치 - 이분탐색
import sys

N, C = map(int, sys.stdin.readline().split())
routers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 공유기 거리를 기준으로 탐색
start = 1
end = max(routers) - min(routers)
answer = start

while start <= end:
    mid = (start + end) // 2
    current = routers[0]  # 현재 위치
    count = 1  # 0번 포함
    # 공유기를 몇 대 설치할 수 있는지 확인
    for i in range(1, N):
        if routers[i] >= current + mid:
            count += 1
            current = routers[i]
    if count >= C:
        if mid > answer:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
