word = 'Serengeti'

for letter in word:
    print(letter)

count = 0

for letter in word:
    vowels = 'aieou'

    if letter in vowels:
        count += 1


print(f'The word {word} has {count} vowels')

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number)

print('odd numbers')
for number in numbers:
    if number % 2 != 0:
        print(number)

days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

for day in days:
    print(day)

person = {
    'name':'Rodrick',
    'age':35,
    'gender':'Male'
}  

for key in person:
    print(f'The value of {key} is {person[key]}')

for n in list(range(10)):
    if n % 2 == 0:
        continue
    print(n)

for n in list(range(10)):
    if n > 5:
        break
    print(n)

for n in list(range(5)):
    print(n)
else:
    print('for loop looping has finished looping')

for n in list(range(5)):
    print(n)
    break
else:
    print('done looping...')
