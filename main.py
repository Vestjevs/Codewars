import re
import numpy as np
import requests
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


def increment_string(strng):
    found = re.findall("[0-9]+", strng)
    if len(found) == 0:
        string = strng + "1"
        return string
    else:
        length = len(found[-1])
        val = int(found[-1])
        val += 1
        string = str(strng[0:len(strng) - len(found[-1])] + '0' * (length - len(str(val))) + str(val))

    return string


def done_or_not(board):  # board[i][j]
    s = "Finished!"
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if not compare(arr, [board[j][i] for j in range(9)]):
            s = "Try again!"
        elif not compare(arr, board[i]):
            s = "Try again!"

    for i in range(0, 9, 3):
        if not compare(arr, board[0 + i][0:3] + board[1 + i][0:3] + board[2 + i][0:3]):
            s = "Try again!"
        elif not compare(arr, board[0 + i][3:6] + board[1 + i][3:6] + board[2 + i][3:6]):
            s = "Try again!"
        elif not compare(arr, board[0 + i][6:9] + board[1 + i][6:9] + board[2 + i][6:9]):
            s = "Try again!"

    return s


def pig_it(word):
    s = []
    arr = word.split(" ")
    for elem in arr:
        if str(elem).isalpha():
            s.append(str(elem)[1:len(str(elem))] + str(elem)[0] + "ay")
        else:
            s.append(str(elem))

    return " ".join(s)


print(pig_it("Hello world !"))
