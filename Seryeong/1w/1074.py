n, r, c = map(int, input().split())

# n - 1을 하는 이유: 2의 N승 * 2의 N승을 4등분하면 2의 N-1승 * 2의 N-1승
# border를 빼는 이유는 재귀함수에서는 해당 사분면만 존재한다고 생각하기 때문


def countNum(n, r, c, num):
    border = (2 ** n) // 2
    if border == 0:
        return num
    # 1사분면
    if (r < border and c < border):
        return countNum(n-1, r, c, num)
    # 2사분면
    if (r < border and c >= border):
        num += (border * border)
        return countNum(n-1, r, c - border, num)
    # 3사분면
    if (r >= border and c < border):
        num += (border * border) * 2
        return countNum(n-1, r - border, c, num)
    # 4사분면
    if (r >= border and c >= border):
        num += (border * border) * 3
        return countNum(n-1, r - border, c - border, num)


print(countNum(n, r, c, 0))
