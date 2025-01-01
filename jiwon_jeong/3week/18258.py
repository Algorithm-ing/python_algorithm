# 백준 18258. 큐 2
# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

N = int(sys.stdin.readline().strip())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        print(-1 if not q else q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1 if not q else 0)
    elif command[0] == 'front':
        print(-1 if not q else q[0])
    else:
        print(-1 if not q else q[-1])