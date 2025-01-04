# 큐 2
import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])
for _ in range(N):
    input = sys.stdin.readline().strip()  # 개행문자 제거
    length = len(queue)
    if input == 'pop':
        if length == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif input == 'size':
        print(length)
    elif input == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif input == 'front':
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif input == 'back':
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        input = input.split()
        queue.append(int(input[1]))
