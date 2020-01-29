import random

n = random.choice(range(10))

for i in range(5):
    c = int(input('Guess a number: '))
    if c==n:
        print('Win')
        exit(n)
    else:
        print('Try again')
print('Lost')
