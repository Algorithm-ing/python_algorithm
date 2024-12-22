N = int(input())
datas = []
answers = []
for _ in range(N):
    action = input()
    if action.startswith("push"):
        data = int(action.split()[-1])
        datas.append(data)
    elif action.startswith("pop"):
        if datas:
            answer = datas.pop()
        else:
            answer = -1
        answers.append(answer)
    elif action.startswith("size"):
        answers.append(len(datas))
    elif action.startswith("empty"):
        if datas:
            answer = 0
        else:
            answer = 1
        answers.append(answer)
    elif action.startswith("top"):
        if datas:
            answer = datas[-1]
        else:
            answer = -1
        answers.append(answer)
    else:
        pass

for answer in answers:
    print(answer)