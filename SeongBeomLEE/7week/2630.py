import sys
input = sys.stdin.readline
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

W = 0
B = 0
def sol(N, maps):
    global W, B
    n = 0
    for map in maps:
        for i in map:
           n += i
    
    if n == N * N:
        B += 1
        return
    elif n == 0:
        W += 1
        return
    else:
        N = N // 2
        # 좌상단
        sol(N, [map[:N] for map in maps[:N]])
        # 우상단
        sol(N, [map[N:2*N] for map in maps[:N]])
        # 좌하단
        sol(N, [map[:N] for map in maps[N:2*N]])
        # 우하단
        sol(N, [map[N:2*N] for map in maps[N:2*N]])

sol(N, maps)
print(W)
print(B)


