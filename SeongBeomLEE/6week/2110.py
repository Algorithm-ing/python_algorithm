import sys
input = sys.stdin.readline
N, C = map(int, input().split())
Xs = []
for _ in range(N):
    Xs.append(int(input()))

Xs = sorted(Xs)
start = 1
end = Xs[-1] - Xs[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    now = Xs[0]
    c = 1
    for i in range(1, N):
        if now + mid <= Xs[i]:
            c += 1
            now = Xs[i]
    
    if C <= c:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)