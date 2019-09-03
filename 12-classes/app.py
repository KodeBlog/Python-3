class Animal:
    def eat(self):
        print('eating')


    def sleep(self):
        print('sleeping')


dog = Animal()

dog.eat()
dog.sleep()

class Myclass:

	def class_method(self):
		print('class method')
		
		
my_class = Myclass()

my_class.class_method()

class MyClass: 
	def __init__(self): 
		print('hello constructor')


	def class_method(self): 
		print('class method') 


my_class = MyClass() 

class MyClass: 
	def __init__(self): 
		print('hello constructor')


	def class_method(self): 
		print('class method') 


	def __del__(self):
		print('shiva the destroyer')


my_class = MyClass() 
my_class.class_method() 

class Arithmetic:
    def add(self,x,y):
        print(x + y)


    def product(self,x,y):
        print(x * y)


    def divide(self,x,y):
        print(x / y)


arithmetic = Arithmetic()
arithmetic.add(2,3)
arithmetic.product(2,3)

class Person:
    _name = ''
    __religion = ''
    country = ''

    def __init__(self, name,religion):
        self._name = name
        self.__religion = religion


    def iam(self):
        print(f'I am {self._name}. My religion is {self.__religion}')


    def get_name(self):
        return self._name
        
        
    def set_religion(self,value):
        self.__religion = value


    def get_religion(self):
        return self.__religion


person = Person('Robert Ingersoll','Agnostic')

print(f'I am {person.get_name()}')
print(f'My religion is {person.get_religion()}')

print(f'My name is {person._name}')
print(f'My religion is {person._Person__religion}')

#Code commented because it raises an exception
"""print(f'My religion is {person.__religion}')"""

class Person:
    __name = ''
    __religion = ''

    def __init__(self, name,religion):
        self.__name = name
        self.__religion = religion


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,value):
        self.__name = value


    def __set_religion(self,religion):
        self.__religion = religion


    def __get_religion(self):
        return self.__religion

    
    def __del_religion(self):
        print('Doing house cleaning before deleting religion property')
        del self.__religion

    docstring_religion = 'Religion property allows you to set, get, and delete the value of __religion variable'
    religion = property(__get_religion, __set_religion, __del_religion,docstring_religion) 


person = Person('Robert Ingersoll','Agnostic')

person.name = 'Thomas Paine'
person.religion = 'Deism'

print(Person.religion.__doc__)
print(f'My religion is {person.religion}, I go by the name of {person.name}')
del person.religion

class Math:
    __sum = 0

    def __init__(self,x,y):
        self.__sum = x + y


    @property
    def sum(self):
        return self.__sum


math = Math(1,2)

print(f'The sum of math is {math.sum}')

class Math:
    __sum = 0
    __product = 0

    def __init__(self,x,y):
        self.__sum = x + y


    @property
    def sum(self):
        return self.__sum


    @classmethod
    def multiplication(cls,x,y):
        cls.__product = x * y
        return cls(x,y)


    @property
    def product(self):
        return self.__product

    @staticmethod
    def square(x):
        return x * x


math = Math(1,2)
print(f'The sum of math is {math.sum}')

p_math = Math.multiplication(3,4)
print(f'The sum of math is {p_math.sum}')
print(f'The product of math is {p_math.product}')

print(f'The square of 35 is {Math.square(35)}')