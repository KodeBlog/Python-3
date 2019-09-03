string_variable = "I'am"    # Evaluates to string based on value
int_variable    = 3         # Evaluates to int based on value
float_variable  = 0.45      # Evaluates to float based on value

print(f'The data type of string_variable is {type(string_variable)} and it has a value of [{string_variable}]')
print(f'The data type of int_variable is {type(int_variable)} and it has a value of [{int_variable}]')
print(f'The data type of float_variable is {type(float_variable)} and it has a value of [{float_variable}]')

number = 2300
print(type(number))

number = 2300.00
print(type(number))

number = 2300j
print(type(number))

first_variable = '"I am" a string'
second_variable = "'I am' a string"
third_variable = '''I 
am
a
string
'''

print(f'first variable [{first_variable}]\n')
print(f'second variable [{second_variable}]\n')
print(f'third variable [{third_variable}]\n')

zen = '"Stop trying to leave, and you will arrive." — Lao Tzu'

print(zen.upper())
print(zen.lower())
print(zen.title())
print(len(zen))

print(zen.find('v'))

cars = ['Toyota','BMW','Benz','Ford']

print(cars)

for car in cars: 
    print(car) 


genres = ('Heavy Metal','R&B','Reggae','Afro Beats')

print(genres[1])

customer = {
    "name":"Rodrick Kazembe",
    "gender":"Male",
    "occupation":"programmer"
}

print(f'The customer name is {customer["name"]}')