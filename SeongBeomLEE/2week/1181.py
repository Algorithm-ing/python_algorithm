N = int(input())
strings = set()
for _ in range(N):
    string = input()
    strings.add(string)

strings = sorted(list(strings), key=lambda string: (len(string), string))
for string in strings:
    print(string)