def app_version():
    print('Version: 1.7')


app_version()

def seo_url(title):
    url = title.lower().replace(' ','-')
    print (url)


seo_url('The life of brian')

def multiply(x,y):
    print(x * y)


multiply(3,3)
multiply(3,4)
multiply(3,5)

def seo_url(title):
    url = title.lower().replace(' ','-')
    print (url)


#Code commented because it raises an exception
"""print (url)"""

def seo_url(title):
    url = title.lower().replace(' ','-')
    return url


title = 'Blessed are the cheese makers'

print(f'The SEO title is {seo_url(title)}')

def the_stoning():
    return 'no one is to stone anybody'
    print ('even if they say jehovah')


print(the_stoning())

squared = (lambda x: x * x) (3)

print(squared)

def square(x):
    return x * x

squared = square(3)

print(squared)

for number in range(5):
    print((lambda x: x * x) (number))

def square(x):
    return x * x

squared = square(3)

ladies = ['Jane','Janet']

def add_lady(lady):
    ladies.append(lady)
    return 


print(f'the original state of ladies is {ladies}\n')

lady = 'Judith'
add_lady(lady)

print(f'The result of add_lady function with param lady and a value of {lady} is \n{ladies}\n')

add_lady(lady)
print(f'The result of add_lady function with param lady and a value of {lady} is \n{ladies}\n')

print(f'the modified state of ladies after calling add_lady is {ladies}')

def count_func(n,m):
    if n > m:
        return 'Counting Completed'
    else:
        print(f'The count is {n}')
        return count_func(n + 1,m)

print(count_func(3,9))

import time

def read_logs():
    print('Application started')
    time.sleep(1)
    print('Bills calculated')
    time.sleep(1)
    print('Bills sent')


read_logs()

def execution_time(func):
    def wrapper():
        start_time = time.asctime(time.localtime(time.time()))
        print(f'Function {func.__name__} execution started at {start_time}')
        func()
        end_time = time.asctime(time.localtime(time.time()))
        print(f'Function {func.__name__} execution finished at {end_time}')

    return wrapper


@execution_time
def read_logs():
    print('Application started')
    time.sleep(1)
    print('Bills calculated')
    time.sleep(1)
    print('Bills sent')
    
read_logs()

def execute_twice(func):
    def wrapper():
        func()
        func()

    return wrapper


@execute_twice
def homer():
    print("D'oh!")

homer()

def awesome_dude(func):
    def wrapper():
        func()
        print('I appreciate you buddy!')
    return wrapper


@awesome_dude
def greet_buddy(name):
    print(f'Hello {name}')


#Code commented because it raises an error
"""greet_buddy('Fernie')"""

def awesome_dude(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('I appreciate you buddy!')
    return wrapper


@awesome_dude
def greet_buddy(name):
    print(f'Hello {name}')


greet_buddy('Fernie')

def generate_numbers():
    yield 2
    yield 4
    yield 6

print(generate_numbers())

for n in generate_numbers():
    print(n)