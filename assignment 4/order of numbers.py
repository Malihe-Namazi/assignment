list=[]
nowL=[]
for i in range (10):
    number=int(input('pleae enter number:'))
    list.append(number)
for i in range (len(list)):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            right=True
    if right==False:
        break
for i in range(len(list)):
    nowL.append(list[i])
print('sort:',nowL)