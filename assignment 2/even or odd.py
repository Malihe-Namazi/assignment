number=int(input('please enter the number:'))
even=0
odd=0
while number>0:
 mod=number%10
 number=number//10
 if(mod%2==0):
     even+=1
 else:
     odd+=1
if(even==odd):
  print('thay are equal.')
elif (even>odd):
  print('even numbers are more than odd numbers')
else:
  print('odd numbers are more than even numbers')
  