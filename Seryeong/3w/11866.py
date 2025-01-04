# 큐 - 요세푸스 문제 0

import sys
from collections import deque

N, K = sys.stdin.readline().split()

queue = deque([])
result = []
for i in range(1, int(N)+1):
    queue.append(str(i))

cnt = 0
while queue:
    popped = queue.popleft()
    cnt += 1
    if cnt == int(K):
        result.append(popped)  # 제거될 사람 저장
        cnt = 0
    else:
        queue.append(popped)

print('<'+', '.join(result)+'>')
