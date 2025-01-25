# 두 용액 - 이분탐색

import sys

N = int(sys.stdin.readline())
sols = sorted(list(map(int, sys.stdin.readline().split())))

if N == 2:  # 두 개일 때
    print(sols[0], sols[1])
else:  # 3개 이상일 때
    small = 0  # 가장 앞부터
    big = N - 1  # 가장 뒤부터
    sum = abs(sols[small] + sols[big])
    smallNum = sols[small]
    bigNum = sols[big]

    while small < big:  # 앞 뒤가 역전되지 않을 때
        if abs(sols[small] + sols[big]) < sum:
            smallNum = sols[small]
            bigNum = sols[big]
            sum = abs(sols[small] + sols[big])
        elif sols[small] + sols[big] < 0:
            small += 1
        else:
            big -= 1

    print(smallNum, bigNum)
