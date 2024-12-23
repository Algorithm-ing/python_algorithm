import sys

N = int(sys.stdin.readline().rstrip())
datas = []
for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    datas.append(data)

answer = 0
right = 0
while datas:
    left = datas.pop()
    if left > right:
        answer += 1
        right = left
print(answer)