east_africa = ['Tanzania','Kenya','Uganda','Rwanda','Burundi']

print(f'Countries that are in east africa include')

for country in east_africa:
    print(country)

cars = ['Toyoto','BMW','Benz','Ford']

print (cars[0])

movies = ['Couples Retreat','Horrible Bosses','40 Year Old Virgin','Last Friday','Shaka Zulu']

print(movies[0:2])

genres = ['Heavy Metal','Symphonic Metal']

genres.append('Black Metal')

print(genres)

genres.insert(0,'Death Metal')

print(genres)

books = ['Think & Grow Rich','The Richest Man in Babylon','Will Power','The Age of Reason']

books.pop(3)

print(books)

import math

squares = [1,4,9,16,25,36]

square_roots = []

for number in squares:
    square_roots.append(math.sqrt(number))

print(square_roots)

import math

squares = [1,4,9,16,25,36]

roots = [math.sqrt(number) for number in squares]

print(roots)

numbers = list(range(11))

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

apps = ['Browser','Email','News','Calculator']

print(f'The list variable apps that {len(apps)} items')

apps = ['Browser','Email','News','Calculator']

print('the original list order is')

print(apps)

apps.reverse()

print('the reversed list order is')

print(apps)

apps = ['Browser','Email','News','Calculator']

print('the original list order is')

print(apps)

apps.sort()

print('the sorted list order is')

print(apps)

apps = ['Browser','Email','News','Calculator']

print('the original list order is')

print(apps)

apps.sort(reverse=True)

print('the sorted list in descending order is')

print(apps)

numbers = list(range(11))

summation = sum(numbers)

print(f'the sum of all the numbers in our list is {summation}')

numbers = list(range(11))

print(f'the minimum number in our list is {min(numbers)}')

numbers = list(range(11))

print(f'the maximum number in our list is {max(numbers)}')

numbers = list(range(11))

def get_even_numbers(number):
    return number % 2 == 0

even_numbers = filter(get_even_numbers, numbers)

print(list(even_numbers))

numbers = list(range(11))

e_numbers = filter(lambda x: x % 2 == 0,numbers)

print(list(e_numbers))