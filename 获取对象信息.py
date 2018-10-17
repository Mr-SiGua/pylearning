# 使用type()
# 首先，我们来判断对象类型，使用type()函数：

# 基本类型都可以用type()判断：
import 继承和多态 as anamail

type(123)
type('str')
type(None)

type(abs)

print(type(anamail.cat))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass

print(type(fn) == types.FunctionType)

type(abs) == types.BuiltinFunctionType

type(lambda x: x) == types.LambdaType

type((x for x in range(10)))==types.GeneratorType

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

# 我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky

print(isinstance(anamail.cat, anamail.Cat))

print(isinstance(anamail.cat, anamail.Animal))
# 能用type()判断的基本类型也可以用isinstance()判断：
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？

# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
# 如果试图获取不存在的属性，会抛出AttributeError的错误：

# 可以传入一个default参数，如果属性不存在，就返回默认值：
# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404
# 也可以获得对象的方法：

# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81

# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

class Student(object):
    name = 'Student'
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print(Student.name) # 打印类的name属性
# Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#Student
# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性