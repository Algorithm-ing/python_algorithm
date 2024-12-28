string = input()
stack = []
pair = []

for i in range(len(string)):  #pop
    stack.append(string[i]) 

TERM = {'[': ']', '(':')'}

total =0
current = 0
nums = []
count = 0

for i in range(len(string)):
    w = stack.pop()
    score =0
    flag = True
    if w == ']' or w ==')':
        if current !=0:
            if len(pair)==0:
                total += current
            else:
                nums.append([current, len(pair)])
        current = 0
        pair.append(w)
        count += 1 
    else:  
        # print(f"count : {count}, total:{total}, current:{current}, stack:{stack}, pair:{pair}, nums : {nums}")
        if len(pair)==0:
            total = 0
            break
        p = pair.pop()
        if TERM[w] != p :
            flag = False
            break
        count -= 1
        score = 3 if p == ']' else 2
        if current == 0:
            current += score
        else:
            current = current * score
            if len(nums)!=0:
                for n in nums:
                    if n[1] == count+1:
                        n[0] = n[0]*score
                        n[1] -= 1
    # print(f"[이후] count : {count}, total:{total}, current:{current}, stack:{stack}, pair:{pair}, nums : {nums}")
    if len(pair)==0 and count ==0:
        total += current
        # nums = [n[0]*score for n in nums]
        for n in nums:
            total += n[0]
        current = 0
        nums = []
    
    if len(stack)==0 and len(pair)!=0:
        total = 0

print(total)