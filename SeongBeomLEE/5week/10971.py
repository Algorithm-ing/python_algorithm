import sys
input = sys.stdin.readline
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))
answers = [[[i], 0] for i in range(N)]
answer = 987654321
while answers:
    now = answers.pop()
    if len(now[0]) == N and W[now[0][-1]][now[0][0]] != 0:
        answer = min(now[1] + W[now[0][-1]][now[0][0]], answer)
        continue
    for i in range(N):
        if i not in now[0] and W[now[0][-1]][i] != 0 and now[1] + W[now[0][-1]][i] <= answer:
            answers.append([now[0][:] + [i], now[1] + W[now[0][-1]][i]])
print(answer)