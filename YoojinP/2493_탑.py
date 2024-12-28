# import sys

# tw = int(input())
# towers = sys.stdin.readline().split(' ')
# towers[-1] = towers[-1][:-1]
# answer = [0] * tw

# head = []
# n_max = -1
# n_idx = -1
# for idx, num in enumerate(towers[::-1]):
#     num = int(num)
#     idx = len(towers)- idx - 1

#     if n_idx == -1:
#         n_idx = idx
#         n_max = num
#         head.append((num, idx))
#     elif n_max < num:
#         h = head.pop()
#         answer[h[1]]= idx + 1
#         for h in head[::-1]:
#             if h[0] < num:
#                 answer[h[1]] = idx + 1
#                 l = head.pop()
#             else:
#                 break
#         n_idx = idx
#         n_max = num
#         head.append((num, idx))
#     else:
#         head.append((num, idx))
#         n_max = num
#         n_idx = idx

# for i in range(len(answer)):
#     term = '' if i == len(answer)-1 else ' ' 
#     print(answer[i], end=term)
    
import sys

tw = int(input())
towers = sys.stdin.readline().split(' ')
towers[-1] = towers[-1][:-1]
answer = [0] * tw

head = []
n_max = -1
for idx, num in enumerate(towers[::-1]):
    num = int(num)
    idx = len(towers)- idx - 1

    if n_max == -1:
        n_max = num
        head.append((num, idx))
    elif n_max < num:
        while len(head)!=0:
            h = head.pop()
            if h[0] < num:
                answer[h[1]]= idx + 1    
            else:
                head.append(h)
                break
        n_max = num
        head.append((num, idx))
    else:
        head.append((num, idx))
        n_max = num

for i in range(len(answer)):
    term = '' if i == len(answer)-1 else ' ' 
    print(answer[i], end=term)
    

    
    