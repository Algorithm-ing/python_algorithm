# 1914. 하노이 탑
# https://www.acmicpc.net/problem/1914
######################## 메모리 초과 ##############################
# import sys
# N = int(sys.stdin.readline().strip())

# def sol(N, start, target, middle, moves):
#     # base case
#     if N == 1:
#         moves.append((start, target))
#         return
#     # n - 1개의 원판을 start -> middle으로 이동
#     sol(N - 1, start, middle, target, moves)
#     # 가장 큰 막대를 start -> target으로 이동
#     moves.append((start, target))
#     # n - 1개의 원판을 middle -> target으로 이동
#     sol(N - 1, middle, target, start, moves)
        
    

# def hanoi_print(N):
#     moves = []
#     sol(N=N, start=1, target=3, middle=2, moves=moves)
#     if N > 20:
#         return len(moves), None
#     else:
#         return len(moves), ' '.join(f"{start} {target}" for start, target in moves)

# length, result = hanoi_print(N=N)
# print(length)
# if result:
#     print(result)
######################## 메모리 초과 ##############################  
import sys
N = int(sys.stdin.readline().strip())

def sol(N, start, target, middle):
    # base case
    if N == 1:
        print(start, target)
        return
    # n - 1개의 원판을 start -> middle으로 이동
    sol(N - 1, start, middle, target)
    # 가장 큰 막대를 start -> target으로 이동
    print(start, target)
    # n - 1개의 원판을 middle -> target으로 이동
    sol(N - 1, middle, target, start)
        
if N > 20:
    print(2 ** N - 1)
else:
    print(2 ** N - 1)
    sol(N, 1, 3, 2)
    