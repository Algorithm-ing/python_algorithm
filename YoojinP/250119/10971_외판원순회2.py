import sys
from itertools import permutations

N = int(sys.stdin.readline())
W = [[0]*N for _ in range(N)]

# 도시 비용 행렬 만들기
for i in range(N):
    nums = list(map(int, sys.stdin.readline().rsplit()))
    W[i][:] = nums


#도시 방문 순서(순열)
combos = permutations([i for i in range(N)], N)

# 최소 비용
minCost = 10000000

#도시 방문 순열을 루프하면서 최소 금액 비교
for combo in combos:
    # 각 도시의 총 비용
    cost = 0
    # 잘못된 경우의 수는 패스하기 위한 flag
    flag = True

    # 시작 도시와 끝 도시 저장
    start = combo[0]
    end = combo[N-1]

    idx = 0
    while idx!= N-1:
        # 도시끼리 연결된 길이 없는 경우
        if W[combo[idx]][combo[idx+1]] == 0:
            flag = False
            break

        cost += W[combo[idx]][combo[idx+1]]
        if cost > minCost:
            flag = False
            break

        # 마지막에는 end-start 길의 비용을 추가
        if idx==N-2:
            if W[end][start] != 0:
                cost += W[end][start]
            else:
                flag = False
                break

        idx += 1

    if flag and minCost > cost:
        minCost = cost
      
print(minCost)