i = 0

while i < 5:
    print(i)
    i += 1

import random

condition = True

while condition:
    n = random.randint(1,7)
    m = random.randint(1,10)

    if (n > m):
        print (f'The winning number is {n}, it was blessed by {m}')
        condition = False
    else:
        print(f'The losing number is {n}, it was jinxed by {m}')

i = 0

while i < 15:
    i += 1

    if (i % 2 == 0):
        continue

    print(i)

while i < 15:
    i += 1

    if (i == 5):
        break

    print(i)

i = 0

while i < 5:
    i += 1

    print(i)
else:
    print('Loop execution has completed successfully')