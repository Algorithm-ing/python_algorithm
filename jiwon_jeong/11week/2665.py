# 백준 2665. 미로만들기
# https://www.acmicpc.net/problem/2665
########################### 다익스트라 ##########################
import sys
from heapq import *

def dijkstra(n, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    costs = {}
    pq = []
    heappush(pq, (0, 0, 0))# 변경 횟수, x좌표, y좌표
    while pq:
        cur_cnt, cur_x, cur_y = heappop(pq)
        
        if cur_x == n - 1 and cur_y == n - 1:
            return cur_cnt
        
        if (cur_x, cur_y) not in costs:
            costs[(cur_x, cur_y)] = cur_cnt
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                
                if 0 <= next_x < n and 0 <= next_y < n:
                    next_cost = cur_cnt + (1 if board[next_x][next_y] == '0' else 0)
                    
                    heappush(pq, (next_cost, next_x, next_y))
                    
def main():
    n = int(sys.stdin.readline().strip())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    print(dijkstra(n=n, board=board))

if __name__ == '__main__':
    main()
########################### 다익스트라 ##########################
    
########################### 0-1 BFS ##########################
# 흰방(1) -> 흰방: 가중치 0
# 검은방(0) -> 흰방: 가중치 1
import sys
from collections import deque
def bfs_01(n, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(0, 0, 0)]) # 변경 횟수, x, y
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = 0
    
    while queue:
        cur_cnt, cur_x, cur_y = queue.popleft()
        
        if cur_x == n -1 and cur_y == n - 1:
            return cur_cnt

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    
                    if board[next_x][next_y] == '0':
                        queue.append((cur_cnt + 1, next_x, next_y))
                    else:
                        queue.appendleft((cur_cnt, next_x, next_y))
                        
def main():
    n = int(sys.stdin.readline().strip())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    print(bfs_01(n=n, board=board))
    
if __name__ == '__main__':
    main()
########################### 0-1 BFS ##########################