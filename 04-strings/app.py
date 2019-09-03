title = 'Zen Fire'
description = "Zen, the master's way of life"
content  = """We seldom realize, for example that our most private thoughts and 
emotions are not actually our own. For we think in terms of 
languages and images which we did not invent, but which were 
given to us by our society - Alan Watts.
"""

print(title)
print(description)
print(content)

title = 'Zen\'s fire'

given_name = "John"
surname = "Doe"

print (given_name + " " + surname)

#Code commented because it raises an exception purpose
"""print ("3" + 3)"""

monty = "spam eggs sausage "

print(monty * 3)

monty = "spam eggs sausage "

print(len(monty))

monty = "Spam eggs sausage"

print(monty.lower())

monty = "Spam eggs sausage"

print(monty.upper())

monty = "Spam eggs sausage"

print(monty.title())

given_name = "John"
surname = "Doe"

print (given_name + " " + surname)

given_name = "John"
surname = "Doe"

print ("{} {}".format(given_name,surname))

given_name = "John"
surname = "Doe"

print ("{1}, {0}".format(given_name,surname))

given_name = "John"
surname = "Doe"

print ("{last}, {first}".format(last=surname,first=given_name))

given_name = "John"
surname = "Doe"

print (f"{given_name}, {surname}")

sum = 2500 * 3

print("The sum is " + str(sum))

brian = "He is not the messiah"

for letter in brian:
    print(letter)


brian = "He is not the messiah"

print(brian[3])

brian = "He is not the messiah"

print(brian[:5])

brian = "He is not the messiah"
print(brian[6:9])

brian = "He is not the messiah"

print(brian[-1])

brian = "He is not the messiah"

print(brian[::-1])

brian = "He is not the messiah"

word_list = brian.split(' ')

print(word_list)

word_list = ['He', 'is', 'not', 'the', 'messiah']

print (' '.join(word_list))

def word_count(text,word):
    count = 0
    for w in text:
        if w == word:
            count += 1
    return count

text = "That's Judith, Mum. Judith, Mother."

word_list = text.split(' ')
word = 'Judith,'

print(f'The word "{word}" appears {word_count(word_list,word)} times in the text "{text}"')
percentage = 100 * word_count(word_list,word) / len(word_list)
print(f'The keyword density of "{word}" is {percentage}%')