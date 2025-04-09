# callable: can it be invoked as a function: class, method, function , lambda function and generator
# returns true if the object arg appears callable
# false then sure the call wil fail not necessarily true for true
# classes are callable reutrning a new instance, instances callable if their class has a __call__() method


# function is not bound to any object, defined with def/lambda called: name(args), no implicit first arg
# method is bound to class or instance of class, self, def, obj.methodname(args)


#  everything is object anyway to see then if this object can be called
# can i call you??


# function
def dummy_func():
    return 'hi'

print("is function callable:",callable(dummy_func))


class MyClass:

    def __init__(self,name):
        self.name=name

    def __call__(self, *args, **kwds):
        # args: positional args tuple
        # **kwargs: keyword args key-value: dictr
        return f'this function does something:{self.name}'
    
    def greet(self):
        print(self.name)


# __init__
obj=MyClass('shraddha')

# instance calling __call__ if this is here we can call it otherwise __init__ touh explicit hai 
obj()

# method bound to an instance
obj.greet()


print("is instance callable:",callable(obj))
print("is class callable:",callable(MyClass)) 
print("is method callable:",callable(MyClass.greet)) 
print("is method callable:",callable(obj.greet)) 
print("is method callable:",callable(MyClass.__class__)) 
print("is method callable:",callable(MyClass.__init__)) 

print('---------')
class MineClass:
    def __init__(self,name):
        self.name=name

    # def __init__(self,name='guest'): optional
    #     self.name=name

    # def __call__():
    #     return 'hi'

    def namaste(self):
        return f'namaste {self.name}'
    
    def hi(self,name):
        return f'hi {name}'

    def hello(self,name):
        print(f'hi {self.name}')
        print(f'hi {name}')
        return



obj2=MineClass('shraddha')
print("is mineclass obj callable now",callable(obj2)) #false 

print(callable(MineClass)) #true

print(obj2.namaste()) #self.name
print(obj2.hi('shraddha'))
print(obj2.hello('shushi'))












# summary:
# 1. callable() to check if object is callable
# 2. __call__ calling instnace as function, instances are callable if they have this
# 3. method and their types: classmethod, staticmethod, instance with self
# 4. function and method difference
# 5. self is sent automatically, self represents this specific instance, and anything attached to self (like self.name) is stored in that object, making it available to all other methods in the class.

# obj2= MineClass() wont pass without name so every time we create an instance 
#  |-----------------|
#  | name            |
#  | functions       |
#  |                 |
#  |-----------------|