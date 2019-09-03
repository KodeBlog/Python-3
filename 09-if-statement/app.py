condition_1 = True

if condition_1:
	print('if condition is true')


condition_1 = False

if condition_1:
    print('condition_1 is true')
else:
    print('condition_1 is false')

condition_1 = True
condition_2 = True

if condition_1:
    print('condition_1 is true')
elif condition_2:
    print('condition_2 is true')
else:
    print('all conditions are false')

condition_1 = True
condition_2 = True

if condition_1 and condition_2:
    print('duff beer')

condition_1 = True
condition_2 = False

if condition_1 and condition_2:
    print('duff beer')

title = 'Database CRUD Application'
print('*' * len(title))
print(title)
print('*' * len(title))
print('')
print('Select an option by entering the option number\n')

options = """1. List all records
2. Search for a record
3. Create new record
4. Update record
5. Delete record
6. Quit
"""

print(options)

selection = input('Enter your selection: ')

if selection == '1':
    print('You selected "List all records"')

elif selection == '2':
    print('You selected "Search for record"')

elif selection == '3':
    print('You selected "Create new record"')

elif selection == '4':
    print('You selected "Update record"')

elif selection == '5':
    print('You selected "Delete record"')

elif selection == '6':
    print('You selected "Quit Application"')


numbers = list(range(11))

for number in numbers:
    if number % 2 == 0:
        print(number)