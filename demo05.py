# 如何快速找到多个字典中的公共建

# 先用随机函数生成字典
from random import randint, sample
from functools import reduce
s1 = {k: randint(1,4) for k in sample('abcdefg', randint(3,6))}
s2 = {k: randint(1,4) for k in sample('abcdefg', randint(3,6))}
s3 = {k: randint(1,4) for k in sample('abcdefg', randint(3,6))}

# 方式一，采用集合操作，使用字典的keys方法，然后求集合的交集
print(s1.keys() & s2.keys() & s3.keys())

# 方式二，采用map()和reduce()
dict_keys = map(dict.keys, [s1, s2, s3])
reduce(lambda a, b: a & b, dict_keys)