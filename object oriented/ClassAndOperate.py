#类和运算符
#python的类运算符也是通过魔法类实现的
class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self,other):
        if isinstance(other,Programer):
            if self.age ==other.age:
                return True
            else:
                return False
        else:
            raise Exception('The Type of object must be Programer')

    def __add__(self,other):
        if isinstance(other,Programer):
            return self.age + other.age
        else:
            raise Exception('The Type of object must be Programer')

if __name__ =='__main__':
    p1 = Programer('chanji', 23)
    p2 = Programer("kitty", 15)
    print(p1==p2)
    print(p1+p2)
