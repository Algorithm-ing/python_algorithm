import sys
input = sys.stdin.readline
N = int(input())
array = sorted(list(map(int, input().split())))

start = 0
end = N - 1
answer = [0, 0]
min = 987654321987654321
while start < end:
    num = array[start] + array[end]
    
    if abs(num) < min:
        min = abs(num)
        answer[0] = array[start]
        answer[1] = array[end]
        if num == 0:
            break
    
    if num < 0:
        start += 1
    else:
        end -= 1

print(*answer)


