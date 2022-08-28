change=input('what do you want to turn into? 1)hours in seconds 2)seconds in hours select: ')
while True:
    if(change=='1'):
       hour=int(input('please enter the hours:'))
       min=int(input('please enter the minute:'))
       sec=int(input('please enter the second:'))
       time=print('your time:',hour,':',min,':',sec,)
       convert=(hour*3600)+(min*60)+sec
       print('hours in seconds is:',convert)
    elif(change=='2'):
        sec=int(input('please enter the seconds:'))
        hour= sec // 3600
        min= (sec % 3600) // 60
        sec= (sec % 3600) % 60
        print('seconds in hours is:',hour,':',min,':',sec)
    else:
      print('please select again.')