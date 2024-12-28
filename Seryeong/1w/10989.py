import sys

n = int(input())
# input을 따로 저장할 공간도 없다
# input = [int(sys.stdin.readline()) for _ in range(n)]

check = [0] * 10001
for _ in range(n):
    i = int(sys.stdin.readline())
    check[i] += 1

# dict의 경우 sort를 다시 해야 함
for i in range(10001):
    if check[i] > 0:
        for _ in range(check[i]):
            print(i)
