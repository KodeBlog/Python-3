import mathemagics

x = 3
y = 7

print (f'The sum of {x} and {y} is {mathemagics.sum(x,y)}')
print (f'The product of {x} and {y} is {mathemagics.product(x,y)}')

from mathemagics import sum, product

x = 3
y = 7

print (f'The sum of {x} and {y} is {sum(x,y)}')
print (f'The product of {x} and {y} is {product(x,y)}')

from fractions import Fraction

print(Fraction(5, 10))

from http import HTTPStatus

print(HTTPStatus.NOT_FOUND.value)

print(HTTPStatus.NOT_FOUND.phrase)

print(HTTPStatus.NOT_FOUND.description)