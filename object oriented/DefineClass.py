


#python中没有属性的权限控制，依靠的是编程规范
class Programer(object) :
    #直接在类中定义的属性，每个类中都有
    hobby = 'Play Computer'

    #通过构造函数定义的属性，每个函数的属性不同
    def __init__(self, name, age, weight):
        #python属性定义
        #可以公开访问的属性
        self.name = name
        #私有属性，但是可以访问
        self._age = age
        #实现部分的私有属性，在类中可以访问，但是new出来的对象中不能访问
        self.__weight = weight
    def get_weight(self):
        return self.__weight

    # python方法定义
    # python中方法的权限也是通过命名规范限制的
    #@classmethod修饰在调用方法的时候直接用类名调用
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    #@property修饰的方法在调用的时候就想调用属性一样，直接加上方法名
    @property
    def get_weight2(self):
        return self.__weight

    def self_introduction(self):
        print('My Name is %s \nI am %s years old\n' % (self.name, self._age))


#l类的继承
class BackendProgramer(Programer):

    #继承并增加参数
    def __init__(self,name,age,weight,language):
        super(BackendProgramer, self).__init__(name,age,weight)
        self.language = language
    #类的多态
    def self_introduction(self):
        print('My Name is %s\n My favourate language is %s' % (self.name,self.language))

#定义一个方法，如果传入的类属于Program的实例，则打印其self_introduction()方法
def introduce(program):
    if isinstance(program,Programer):
        program.self_introduction()


if __name__ =='__main__':
    programer = Programer('Albert', 25, 80)
    #访问python中的属性
    #对象中所有的属性
    print(dir(programer))
    #构造函数中的属性名称和值
    print(programer.__dict__)
    #使用封装方法获取属性值
    print(programer.get_weight())
    #直接访问“私有属性”
    print(programer._Programer__weight)

    #访问python中的方法
    #直接通过对象名称访问
    print(Programer.get_hobby())
    #新建对象，通过方法名称访问
    print(programer.get_weight2)

    #访问普通的方法
    programer.self_introduction()

    #类的继承
    print("类的继承")
    backendProgramer = BackendProgramer('Albert',25,80,'python')
    print(dir(backendProgramer))
    print(backendProgramer.__dict__)
    print(type(backendProgramer))
    print(isinstance(backendProgramer,Programer))

    #多态
    introduce(programer)
    introduce(backendProgramer)





