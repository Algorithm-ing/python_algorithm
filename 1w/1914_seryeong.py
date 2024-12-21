k = int(input())


def hanoi(num, start, end, other):
    if num == 0:
        return
    # 가장 큰 원판을 제외한 나머지 원판을 other로 일단 치워두기
    hanoi(num-1, start, other, end)
    print(start, end)
    # 가장 큰 원판을 제외한 나머지 원판을 일단 치워둔 other에서 end 위에 얹기
    hanoi(num-1, other, end, start)


print(2**k - 1)  # 배열에 담아서 개수를 셀 경우 메모리 초과(계차수열)
if k <= 20:
    hanoi(k, 1, 3, 2)
