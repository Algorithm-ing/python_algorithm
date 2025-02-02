import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
preoder = []
while True:
    try:
        preoder.append(int(input()))
    except:
        break
def postorder(nodes:list[str]):
    if not nodes:
        return
    root = nodes[0]
    left_nodes = []
    right_nodes = []
    for index in range(len(nodes)):
        if index == 0:
            continue
        if nodes[index] > root:
            left_nodes = nodes[1:index]
            right_nodes = nodes[index:]
            break
    else:
        left_nodes = nodes[1:]
    postorder(left_nodes)
    postorder(right_nodes)
    print(root)

postorder(preoder)