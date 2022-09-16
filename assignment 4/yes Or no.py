count1=1
count2=1
list=[]
for i in range (10):
    number=int(input('please enter the numbers:'))
    list.append(number)
    
for a in range(9):
    if(list[a] <= list[a+1]):
        count1+=1
        continue
    elif(list[a] >= list[a+1]):
        count2+=1
        continue
    else:
        break
    
if(count1==10)or(count2==10):
    print('yes')
else:
    print('no')
        
