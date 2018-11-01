# 如何统计序列中元素出现的频度
# 使用collections模块中的Counter可以快速找出列表中元素出现的次数
# 使用most_common()可以快速获取出现最多次数的元素

from random import randint
from collections import Counter
data = [randint(0, 20) for _ in range(30)]
c = Counter(data) 
max = c.most_common(3)