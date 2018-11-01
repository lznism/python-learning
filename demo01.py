# 如何在列表，字典，集合中根据条件筛选数据

# 列表解析
def get_positive(data):
    """过滤list获取正数列表，列表解析效率更高"""
    # return filter(lambda x: x >= 0, data)
    return [x for x in data if x >= 0] # 效率更高

# 字典解析
def get_dict(d):
    """过滤出字典中值大于90的元素"""
    return {k: v for k, v in d.iteritems() if v > 90}

# 集合解析
def get_set(s):
    """过滤出集合中可以被3整除的数"""
    return {x for x in s if x % 3 == 0}

