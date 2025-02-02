import sys

A, B, C = map(int, sys.stdin.readline().split())

dict = {}
dict['1'] = A % C


def divide_and_conquer(multiple):
    numOne = str(int(multiple) // 2)
    numTwo = str(int(multiple) - int(numOne))

    if numOne in dict:
        numOneMultiple = dict[numOne]
    else:
        numOneMultiple = divide_and_conquer(numOne)

    if numTwo in dict:
        numTwoMultiple = dict[numTwo]
    else:
        numTwoMultiple = divide_and_conquer(numTwo)

    result = (numOneMultiple % C) * (numTwoMultiple % C) % C
    if multiple not in dict:
        dict[multiple] = result
    return result


if B == 1:
    print(A % C)
else:
    print(divide_and_conquer(B))
