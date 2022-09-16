number=int(input('please enter the number:'))
fact = number
for i in range(1,number-1):
    fact = fact / i
    if fact==1:
        c=True
        break
    else:
        c=False
        
if c==True:
    print("yes")
else:
    print('no')