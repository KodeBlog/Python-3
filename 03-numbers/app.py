int_var = -6; float_var = 1.3 ; complex_var = 1 + 3j

print(f'The type of int_var is {type(int_var)} and it has a value of {int_var}')
print(f'The type of float_var is {type(float_var)} and it has a value of {float_var}')
print(f'The type of complex_var is {type(complex_var)} and it has a value of {complex_var}')
print(f'The complex_var has a real value of {complex_var.real} and imaginary part of {complex_var.imag}')

hours = 20.6
hourly_rate = 120.00

total_wages = hours * hourly_rate

print(f'The total charge for {hours} hours at the rate of {hourly_rate} is {total_wages:,}')

result = 7 + 1 * 2 / 4

print(result)

first_number = 1
second_number = 2.0

total = first_number + second_number

print(f'The sum of {first_number} {type(first_number)} and {second_number} {type(second_number)} is {total} {type(total)}')

total = int(first_number + second_number)

#This code raises an exception on purpose that why its commented
"""header = "Value Added Tax (VAT) Calculator"

print(header)
print('*' * len(header))
print('')

vat_rate = 0.18
amount = input('Enter the total amount: ')
vat_charge = amount * vat_rate

print(f'The VAT is {vat_charge:,} ({vat_rate * 100}% of {amount:,})')"""

header = "Value Added Tax (VAT) Calculator"

print(header)
print('*' * len(header))
print('')

vat_rate = 0.18
amount = input('Enter the total amount: ')
amount = float(amount)
vat_charge = amount * vat_rate

print(f'The VAT is {vat_charge:,} ({vat_rate * 100}% of {amount:,})')

import random

print(f'Python random module generated {random.random()}')

numbers = [1,2,3,4,5]

print(type(numbers))

total = sum(numbers)

print(f'The sum is {total}')

print(f'The min is {min(numbers)}')

print(f'The max is {max(numbers)}')