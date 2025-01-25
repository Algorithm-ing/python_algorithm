# 백준 2110. 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys
N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(N)]

def can_install_router(houses, C, distance):
    cnt = 1
    tmp = houses[0]
    for house in houses[1:]:
        if house - tmp >= distance:
            cnt += 1
            tmp = house
        if cnt >= C:
            return True
    return False


def sol(C, houses):
    houses.sort()
    low, high = 1, houses[-1] - houses[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_install_router(houses, C, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

print(sol(C=C, houses=houses))