# 큐 - 카드2
import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])
for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()  # 제일 위 카드 버리기
    popped = queue.popleft()
    queue.append(popped)  # 제일 위 카드를 제일 아래로 옮기기

print(queue[0])
