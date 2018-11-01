# 如何让字典保持有序
# OrderedDict是有序的字典
from collections import OrderedDict
d = OrderedDict()

from time import time
from random import randint
players = list('abcdefgh')
start = time()

for i in range(8):
    input()
    p = players.pop(randint(0, 7-i))
    end = time()
    print(i+1, p, end - start)
    d[p] = (i+1, end - start)