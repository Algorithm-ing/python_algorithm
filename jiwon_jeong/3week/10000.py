# 백준 10000. 원 영역
# https://www.acmicpc.net/problem/10000
import sys
N = int(sys.stdin.readline().strip())
circles = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
def sol(N, circles):
    events = []
    for x, r in circles:
        events.append((x - r, 1))
        events.append((x + r, -1))
        
    events.sort(key=lambda e: (e[0], e[1] == 1))
    
    cnt = 1
    stack = []
    for event in events:
        if event[1] == 1: # 원이 열림: (
            stack.append(event)
        else: # 닫히는 원이 들어왔을 때: )
            cum_width = 0
            while stack:
                prev = stack.pop()
                
                if prev[1] == 1: # 이전께 열리는 원('(')이라면
                    width = event[0] - prev[0]
                
                    if width == cum_width: # 현재 닫히는 원이 이전 원들과 정확히 접하는 상태 : 내부 + 외부
                        cnt += 2
                    else:                  # 현재 원이 이전 원들과 겹치거나 독립적인 경우
                        cnt += 1
                
                    stack.append((width,'C')) # 폭 계산
                    break

                elif prev[1] == 'C': # 
                    cum_width += prev[0]
    return cnt
print(sol(N=N, circles=circles))