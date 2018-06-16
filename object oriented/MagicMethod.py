#python中魔法方法使用双下划线开始和结束，如__init__
#python实例化过程为，先使用__new__方法创建类的实例，然后使用__init__初始化对象
class Programer(object):
    #魔法方法new方法
    def __new__(cls, *args, **kwargs):
        print('call_new_method')
        print(args)
        return super(Programer, cls).__new__(cls)

    def __init__(self,name,age):
        print('call_init_method')
        self.name = name
        self.age = age

#类的展现，转化为字符串__str__:转化为人看的子符串，__repr__转化为机器识别的字符串，__unicode__
#展现对象的属性__dir__
    def __str__(self):
        return '%s is %s years ld' % (self.name,self.age)
    def __dir__(self):
        return self.__dict__.keys()



if __name__ =='__main__':
    programer = Programer('chanji',23)
    print(programer.__dict__)

    print(programer)
    print(dir(programer))