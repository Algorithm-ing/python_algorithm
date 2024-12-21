"""
- 게속 4등분씩 탐색하고, 왼상단으로 이동하면됨
- 하나의 블록을 다 탐색하는 경우의 수는 해당 블록의 개수
"""

def solution(N:int, r:int, c:int):
    if N == 0:
        return 0
    half = 2 ** (N - 1)
    # 왼상단
    if r < half and c < half:
        return solution(N - 1, r, c)
    # 오상단의 경우 왼상단은 이미 탐색했다고 할 수 있음
    if r < half and c >= half:
        return 1 * half * half + solution(N - 1, r, c - half)
    # 왼하단의 경우 왼상단, 오상단은 이미 탐색했다고 할 수 있음
    if r >= half and c < half:
        return 2 * half * half + solution(N - 1, r - half, c)
    # 오하단의 경우 왼상단, 오상단, 왼하단은 이미 탐색했다고 할 수 있음
    if r >= half and c >= half:
        return 3 * half * half + solution(N - 1, r - half, c - half)
N, r, c = map(int, input().split())
print(solution(N, r, c))
