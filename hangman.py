import random

strs = ['1','2','3','4','5']
count = 0
string = random.choice(strs)

for i in range(5):
    c = input('Enter a number: ')
    if c in string and c!='':
        print('Good')
        counts = count + 1
        if count == 3:
            break
    else:
        print('You entered a wrong number')
        
if count == 3:
    print('Won')
else:
    print('Lost')
