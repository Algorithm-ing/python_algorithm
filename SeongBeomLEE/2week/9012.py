T = int(input())
answers = []
for _ in range(T):
    strings = input()
    is_vps = "YES"
    datas = []
    for string in strings:
        if string == "(":
            datas.append(string)
        else:
            if datas:
                datas.pop()
            else:
                is_vps = "NO"
                break
    else:
        if datas:
            is_vps = "NO"
    answers.append(is_vps)

for answer in answers:
    print(answer)