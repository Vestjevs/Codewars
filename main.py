from functools import partial
from random import random, randint
from fractions import Fraction
import operator as op

import numpy as np


def example(i):
    return f'{random.random():.{i}f}'


class TripleElementListIteration:
    def __init__(self, lst):
        self.__lst = lst
        self.__length = 0

    def __next__(self):
        if self.__length < len(self.__lst):
            self.__length += 1
            return self.__lst[self.__length - 1]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return TripleElementListIteration(self)


def random_generator(k):
    for i in range(k):
        yield randint(1, 100)


arr = [("John", "Malcolm", " Andrew"), ("Vest", "Jevs"), ("Svejentsev", "Aleksey")]

length = lambda x: len(''.join(x))

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(arr)
sort_by_last(arr)
print(arr)

y = ['ara', 'assh', 'asdnb']
sort_by_last(y)
print(y)
print(np.log(7))
