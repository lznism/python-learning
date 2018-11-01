# 如何为元组中的每个元素命名来提高程序的可读性
# 比如我们会在一个元组中定义学生的名字，年龄，性别

student = ('Jim', 16, 'male', 'jim888@gmail.com')

# 通常如果我们需要访问上面这个元组中的元素，我们会用索引0,1,2,3，但这样的话，就降低了可读性
# 这里我们可以定义一些常量来避免这些，提高程序的可读性

# 方法一
NAME, AGE, SEX, EMAIL = range(0,4)
# name
print(student[NAME])

# age
if student[AGE] > 12:
    pass

# sex
if student[SEX] == 'male':
    pass

# 方法二 使用标准库中collections.nametuple替代内置tuple
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'jim888@126.com')
# Student(name='Jim', age=16, sex='male', email='jim888@126.com')

# 下面我们就可以使用属性的方式访问了
s.name
s.age
s.sex
s.email
isinstance(s, tuple) # True