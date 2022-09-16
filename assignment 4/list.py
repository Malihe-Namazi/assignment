import random
Len=int((input('please enter the counter:')))
list=[]
counter=0
while (Len > counter) :
   num=random.randint(0,99)
   if (num in list):
       print('try again')
            
   else:
      list.append(num)
      counter+=1
print(list)