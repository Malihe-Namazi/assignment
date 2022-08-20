win=0
loss=0
equal=0
score=0
counter=1
point=0
while counter<=8:
    print('please enter the result\n(win=3,equal=1 ,loss=0)',counter)
    point=int(input('your point:'))
    print('----------------------------------------')
    
    if point==3:
      win+=1
      score+=1
      counter+=1
    elif point==0:
      loss+=1
      score+=0
      counter+=1
    elif point==1:
      equal+=1
      score+=1
      counter+=1
    else:
      print('please try again.')
      counter-=1
      counter+=1
print('your fanail score is:',score,'\n and the result of games.\n your wins:',win,' \n your loss:',loss, '\n equal point:',equal)