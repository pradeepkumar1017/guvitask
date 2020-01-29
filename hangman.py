
import random
strs = ['A','B','C','D','E','F']
count = 0
string = random.choice(strs)

for i in range(5):
    c = input('Enter a character: ')
    if c in string and c!='':
        print('Good')
        counts = count + 1
        if count == 3:
            break
    else:
        print('You entered a wrong character')
        
if count == 3:
    print('Won')
else:
    print('Lost')
