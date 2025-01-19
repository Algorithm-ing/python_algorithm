"""
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function

```
- The local variables are stored in a fixed-size array (not a dict). Then retrieving a local variable is literally a pointer lookup into the list and a refcount increase on the PyObject which is trivial.
- Contrast this to a global lookup (LOAD_GLOBAL), which is a true dict search involving a hash and so on.
```

파이썬에서는 전역변수를 사용하는 것 보다, 지역변수를 사용하는 것이 조금 더 빠를 수 있다.

아래 코드를 def 로 감싼 코드가 더 속도가 빠름
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))
max_trees = [] # mid 보다 큰 나무를 저장
min_trees = trees[:] # mid 보다 작거나 같은 나무를 저장

start = 1
end = max(trees)
H = 0
while start <= end:
    mid = (start + end) // 2

    while True:
        if not min_trees and max_trees[-1] > mid:
            break
        if not max_trees and min_trees[-1] <= mid:
            break
        if min_trees and max_trees and min_trees[-1] <= mid and max_trees[-1] > mid:
            break
        if min_trees and min_trees[-1] > mid:
            max_trees.append(min_trees.pop())
        if max_trees and max_trees[-1] <= mid:
            min_trees.append(max_trees.pop())
    
    total = 0
    for tree in max_trees:
        total += tree - mid
    
    if total >= M:
        H = mid
        start = mid + 1
    else:
        end = mid - 1
print(H)