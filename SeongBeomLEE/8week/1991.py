import sys
input = sys.stdin.readline
N = int(input())
trees = []
root_to_index = {}
for index in range(N):
    trees.append(input().split())
    root_to_index[trees[-1][0]] = index

# 전위 순회
answer = ""
def preoder(root):
    global answer
    if root == ".":
        return
    answer += root
    # 왼쪽 노드 탐색
    preoder(trees[root_to_index[root]][1])
    # 오른쪽 노드 탐색
    preoder(trees[root_to_index[root]][2])
preoder("A")
print(answer)

# 중위 순회
answer = ""
def inorder(root):
    global answer
    if root == ".":
        return
    # 왼쪽 노드 탐색
    inorder(trees[root_to_index[root]][1])
    answer += root
    # 오른쪽 노드 탐색
    inorder(trees[root_to_index[root]][2])
inorder("A")
print(answer)

# 후위 순회
answer = ""
def postorder(root):
    global answer
    if root == ".":
        return
    # 왼쪽 노드 탐색
    postorder(trees[root_to_index[root]][1])
    # 오른쪽 노드 탐색
    postorder(trees[root_to_index[root]][2])
    answer += root
postorder("A")
print(answer)