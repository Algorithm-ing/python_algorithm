# 트리 순회 - 그래프 탐색

import sys

N = int(sys.stdin.readline())
trees = [sys.stdin.readline().split() for _ in range(N)]

preResult = ''
# 전위 순회 루트/왼쪽/오른쪽


def preOrder(tree):  # 첫 줄만 받음
    global preResult
    preResult += tree[0]
    if tree[1]:
        for i in trees:
            if tree[1] == i[0]:
                preOrder(i)
                break
    if tree[2]:
        for i in trees:
            if tree[2] == i[0]:
                preOrder(i)
                break


preOrder(trees[0])
print(preResult)

inResult = ''
# 중위 순회 왼쪽/루트/오른쪽


def inOrder(tree):
    global inResult
    if tree[1]:
        for i in trees:
            if tree[1] == i[0]:
                inOrder(i)
                break
    inResult += tree[0]
    if tree[2]:
        for i in trees:
            if tree[2] == i[0]:
                inOrder(i)
                break


inOrder(trees[0])
print(inResult)

postResult = ''
# 후위 순회 왼쪽/오른쪽/루트


def postOrder(tree):
    global postResult
    if tree[1]:
        for i in trees:
            if tree[1] == i[0]:
                postOrder(i)
                break
    if tree[2]:
        for i in trees:
            if tree[2] == i[0]:
                postOrder(i)
                break
    postResult += tree[0]


postOrder(trees[0])
print(postResult)
