#10989_수 정렬하기3

# 계수 정렬
import sys 

N = int(input())

a = []
c = [0 for i in range(N)]

for _ in range(N):
    a.append(int(sys.stdin.readline()))

a_max = max(a)
b = [0 for i in range(a_max)]

for i in range(N):
    b[a[i]] += 1

for i in range(len(b)):
    b[i] = b[i] + b[i-1]
    
for i in range(N):
    c[b[a[i]]] = a[i]
    b[a[i]] -= 1

for i in range(N):
    print(c[i])
