import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque([])
for _ in range(N):
    action = input()
    if action.startswith("push"):
        queue.append(action.split()[-1])
    elif action.startswith("pop"):
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif action.startswith("size"):
        print(len(queue))
    elif action.startswith("empty"):
        if queue:
            print(0)
        else:
            print(1)
    elif action.startswith("front"):
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif action.startswith("back"):
        if queue:
            print(queue[-1])
        else:
            print(-1)