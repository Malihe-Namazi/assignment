
password=[1,2,3,4]
upside=[4,3,2,1]
counter=0
pas=[]
while (counter<3):
    for i in range(4):
       p=int(input('please enter the password:'))
       pas.append(p)
    if (pas==password):
      print('welcome :)')
    elif(pas==upside):
        print('we are calling the police!!!!!!!!!!!!')
    else:
        print('password is incorrect')
        counter=counter+1
if(counter>2):
    print('access denied')