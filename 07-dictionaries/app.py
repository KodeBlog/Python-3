results = {
    'maths':89,
    'chemistry':75,
    'biology':95,
    'physics':90
}

print(type(results))

print(results)

results = {
    'maths':89,
    'chemistry':75,
    'biology':95,
    'physics':90
}

#iterate through all the keys
print('the keys in our dictionary are')
for key in results:
    print(key)

results = {
    'maths':89,
    'chemistry':75,
    'biology':95,
    'physics':90
}

#print keys and corresponding values
print('the keys and their values in our dictionary are\n')
for key in results:
    print(f'The score for {key} is {results[key]}')

drinks = {
    'beer':'Castle',
    'vodka':'Russian Standard',
    'gin':'London Dry Gin',
    'rum':'Barcadi'
}

print(drinks)
item = drinks.pop('beer')
print(f'the item {item} has been removed from the dictionary')
print(drinks)

drinks = {
    'beer':'Castle',
    'vodka':'Russian Standard',
    'gin':'London Dry Gin',
    'rum':'Barcadi'
}

print(drinks)
del drinks['rum']
print(drinks)

arts = {
    'trivium':['Grammar','Logic','Rhetoric'],
    'quadrivium':['Arithmetic','Geometry','Astronomy','Music']
}

arts['remarks'] = 'Gone are the days when the liberal arts where central to university learning.'

print(arts)

arts = {
    'trivium':['Grammar','Logic','Rhetoric'],
    'quadrivium':['Arithmetic','Geometry','Astronomy','Music']
}

arts['remarks'] = 'Gone are the days when the liberal arts where central to university learning.'

for key in arts:
    print(key)

    if key == 'remarks':
        print(arts[key])
        continue

    for art in arts[key]:
        print(f'-{art}')

numbers = [1,2,3,4,5,6,7,8,9,10]

roots_squared = {n: n**2 for n in numbers}

print(roots_squared)

numbers = [1,2,3,4,5,6,7,8,9,10]

odds_squared = {x: x**2 for x in numbers if x % 2 != 0}

print(odds_squared)

pets = {
    'cats':'Disliked',
    'dogs':'Liked',
    'snakes':'Loved'
}

print(pets)

pets.clear()

print(pets)

pets = {
    'cats':'Disliked',
    'dogs':'Liked',
    'snakes':'Loved'
}

keys = pets.keys()

print(keys)

pets = {
    'cats':'Disliked',
    'dogs':'Liked',
    'snakes':'Loved'
}

values = pets.values()

print(values)

pets = {
    'cats':'Disliked',
    'dogs':'Liked',
    'snakes':'Loved'
}

print(pets.get('snakes'))

pets = {
    'cats':'Disliked',
    'dogs':'Liked',
    'snakes':'Loved'
}

pets.pop('cats')

print(pets)