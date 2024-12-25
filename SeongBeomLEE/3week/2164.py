from collections import deque
N = int(input())
queue = deque([i + 1 for i in range(N)])
cnt = 0
while len(queue) != 1:
    if cnt % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    cnt += 1
print(queue[0])