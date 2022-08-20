number=int(input('please enter the number:'))
first_number=number
reverse=0
while(number>0):
    mod= number % 10
    reverse = (reverse * 10) + mod
    number = number // 10
if first_number==reverse:
     print('your number and its reverse are match.')
else:
    print('your number',first_number,'and its reverse',reverse,'are not match.')