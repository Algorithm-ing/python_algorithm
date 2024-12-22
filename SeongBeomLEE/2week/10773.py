K = int(input())
datas = []
for _ in range(K):
    data = int(input())
    if data == 0:
        if datas:
            datas.pop()
    else:
        datas.append(data)
print(sum(datas))