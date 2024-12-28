import sys

test_case = int(input())
lines = []
answer = []

def judge(string, arr):
    if len(string)==0:
        flag = True if len(arr)==0 else False
        return flag
    if string[-1]==')':
        arr.append(')')
        return judge(string[:-1], arr)
    elif string[-1]=='(':
        if len(arr)==0:
            return False
        arr = arr[:-1]
        return judge(string[:-1], arr)
    else:
        return False

for t in range(test_case):
    line = sys.stdin.readline()
    lines.append(line[:-1]) # '/n' 없애버리기
    
print(f"line:{lines}")
for line in lines:
    stack = []
    anw = 'YES' if judge(line, stack) else 'NO'
    answer.append(anw)
        
for a in answer:
    print(a)