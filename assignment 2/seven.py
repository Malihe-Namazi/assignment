 
number=int(input('please enter the number:')) 
mod=number/7
next_number=((number//7)*7)+7
if (mod==0):
   print('this number is multiple of seven.')
else:
   print('this number is not multiple of seven, the next number is:',next_number)
   