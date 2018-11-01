# 如何根据字典中值得大小，对字典中的项进行排序
# sorted函数可以传递第二个参数，第二个参数可以是一个lamda函数

d = {
    'a': 1,
    'c': 3,
    'b': 2
}

def sort(d):
    return sorted(d.items(), key=lambda x: x[1])
