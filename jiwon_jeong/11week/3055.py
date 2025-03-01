# 백준 3055. 탈출
# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
def bfs_flood_and_escape(R, C, forest):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue_water, queue_gosum = deque(), deque()
    water_time = [[-1] * C for _ in range(R)]
    gosum_time = [[-1] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if forest[r][c] == '*':
                queue_water.append((r, c))
                water_time[r][c] = 0
            elif forest[r][c] == 'S':
                queue_gosum.append((r, c))
                gosum_time[r][c] = 0
            elif forest[r][c] == 'D':
                end_x, end_y = r, c
                
    while queue_water:
        cur_x, cur_y = queue_water.popleft()
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < R and 0 <= next_y < C:
                if water_time[next_x][next_y] == -1 and forest[next_x][next_y] not in ('X', 'D'):
                    water_time[next_x][next_y] = water_time[cur_x][cur_y] + 1
                    queue_water.append((next_x, next_y))
    
    while queue_gosum:
        cur_x, cur_y = queue_gosum.popleft()
        
        if (cur_x, cur_y) == (end_x, end_y):
            return gosum_time[cur_x][cur_y]
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < R and 0 <= next_y < C:
                if gosum_time[next_x][next_y] == -1 and forest[next_x][next_y] not in ('X', '*'):
                    if water_time[next_x][next_y] == -1 or gosum_time[cur_x][cur_y] + 1 < water_time[next_x][next_y]:
                        gosum_time[next_x][next_y] = gosum_time[cur_x][cur_y] + 1
                        queue_gosum.append((next_x, next_y))
    
    return "KAKTUS"
    
def main():
    R, C = map(int, sys.stdin.readline().split())
    forest = [list(sys.stdin.readline().strip()) for _ in range(R)]
    
    print(bfs_flood_and_escape(R, C, forest))

if __name__ == '__main__':
    main()