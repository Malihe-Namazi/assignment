username='malihe namazi'
password=99154291
counter=0
while (counter<3):
  name=input('please enter username:')
  pas=int(input('please enter the password:')) 
  if (name==username) and (pas==password):
    print('welcom')
    break
  else:
    print('password or username is incorrect')
  counter=counter+1
if(counter>2):
    print('access denied')