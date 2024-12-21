N = int(input())

visit1 = [False] * (N + 1) # 열 가능 여부
visit2 = [False] * (2 * N + 1) # 우측 대각선 가능 여부
visit3 = [False] * (2 * N + 1) # 좌측 대각선 가능 여부

answer = 0

def solution(visit1, visit2, visit3, count):
    global answer
    if count == (N + 1): 
        answer += 1 # row 4까지 완료 되어야 모든 경우의 수를 다 탐색했다고 볼 수 있음
    if count <= N:
        for col in range(1, N + 1):
            if not visit1[col]:
                if not visit2[count + col]: 
                    if not visit3[count - col + N]:
                        visit1[col] = True
                        visit2[count + col] = True
                        visit3[count - col + N] = True
                        solution(visit1, visit2, visit3, count + 1)
                        visit1[col] = False
                        visit2[count + col] = False
                        visit3[count - col + N] = False

count = 1
for col in range(1, N + 1):
    visit1[col] = True
    visit2[count + col] = True
    visit3[count - col + N] = True
    solution(visit1, visit2, visit3, count + 1)
    visit1[col] = False
    visit2[count + col] = False
    visit3[count - col + N] = False

print(answer)