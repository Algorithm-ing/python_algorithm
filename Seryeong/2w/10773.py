# 제로
K = int(input())

book = []
sum = 0
for _ in range(K):
    num = int(input())
    if num == 0:
        poppedNum = book.pop()
        sum -= poppedNum
    else:
        book.append(num)
        sum += num

print(sum)
