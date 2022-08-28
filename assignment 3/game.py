import random

counter=0
small=0
big=99
print('please choose a number between (0,99).')

while True:
    number=random.randint(small,big)
    print('computer gusse:',number)
    counter+=1
    ansower=input('select one option: \n T)true F)false\n select:')
    if(ansower=='T'):
        print('I guessed right ;)',counter)
        break
    elif(ansower=='F'):
        num=input('which one?  \n 1)number is bigger 2)number is smaller \n select: ')
        if(num=='1'):
           small=number
           number=random.randint(small+1,big-1)
           counter+=1
        elif(num=='2'):
            big=number
            number=random.randint(small+1,big-1)
            counter+=1
        else:
            print('please try again.')
            counter-1
            continue
    else:
        print('please try again.')
        counter-1
        break
        