#类的属性控制
class Programer(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self, name):
        #死循环
        #return getattr(self,name)
        #死循环
        #return  self.__dict__[name]
        #right
        return super(Programer, self).__getattribute__(name)

    def __setattr__(self, name, value):
        #死循环
        #setattr(self,name,value)
        self.__dict__[name] = value

if __name__ =='__main__':
    p = Programer('Albert',25)
    print(p.name)