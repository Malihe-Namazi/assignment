import random
sum=0
counter=0
while True:
    number=random.randint(1,6)
    print('numbers:',number)
    if(number<6):
       sum+=number
       counter+=1
    else:
        break
print('sum is:',sum,'\t \t counter:',counter)