attributes = ('id','name','username','email','password')

print(type(attributes))

print(attributes)

#Code commented because it raises an exception
"""attributes = ('id','name','username','email','password')

attributes[3] = 'created_at'"""

attributes = ('id','name','username','email','password')

attr = list(attributes)

attr[3] = 'created_at'

attributes = tuple(attr)

print(type(attributes))

print(attributes)

attributes = ('id','name','username','email','password')

print(f'the second item is {attributes[1]}')

attributes = ('id','name','username','email','password')

#Code commented because it raises an exception
"""print(f'the second item is {attributes[9]}')"""

attributes = ('id','name','username','email','password')

print('created_at' in attributes)

attributes = ('id','name','username','email','password')

for attribute in attributes:
    print(attribute)

values = ('1','Natasha','katie','amanda@example.com')

(id,name,username,email) = values

print('user details\n')
print(f'id: {id}')
print(f'name: {name}')
print(f'username: {username}')
print(f'email: {email}')

values = ('1','Natasha','katie','amanda@example.com')

print(len(values))

letters = ('alef','bet','gimel','dalet','he','vav','zayin','chet','tet','yod','kaf')

print('the original tuple is ')
print(letters)
print('the sorted tuple is')
letters = tuple(sorted(letters)) 
print(letters)