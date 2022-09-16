list=['ali','atefe','reza','homa','amir','fateme']
print(list)
for i in range(3):
    name=input('enter the name:')
    num=int(input('choose the part you eant:'))
    list.insert(num,name)
    print(list)