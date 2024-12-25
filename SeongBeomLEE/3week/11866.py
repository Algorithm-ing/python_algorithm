from collections import deque
N, K = map(int, input().split())
queue = deque([i + 1 for i in range(N)])
result = []
cnt = 1
while queue:
    now = queue.popleft()
    if cnt % K == 0:
        result.append(str(now))
    else:
        queue.append(now)
    cnt += 1
print("<" + ", ".join(result) + ">")


