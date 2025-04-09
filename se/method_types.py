# methods are bound to instances
# methods have a  implicit first argument: self

# instance method: self needs no @classdecorator, access/modiy object state
# class method no self, @classmethod access/modiy class state
# static method slef no, @staticmethod, utility helper



class Person:
    # instance class, inidividual copies for each
    def __init__(self,name):
        self.name=name
    
    def hi(self):
        return f'Hi, customer{self.name}'

class Cake:
    # all instances the same count because it is class level
    count:int=0

    @classmethod
    def sale(cls):
        cls.count+=1

class Wazowski:
    @staticmethod
    def scream(a:int):
        return "scream "*a
    

# instance class
p=Person('sushi')
p.hi()

# class method: class level sharing
C=Cake()
C.sale()
C.sale()
print(C.count)
print(Cake.count)

# static method 
w=Wazowski()
print(Wazowski.scream(4))
print(w.scream(3))