import sys
a:int = int(sys.stdin.readline())
arr = []
for _ in range(a):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):
   sys.stdout.write(str(i) + '\n')
