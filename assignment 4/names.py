name1 = []
name2 = []
number = int (input('how many names do you want to enter ?\n '))
for i in range(number):
    name = input('please enter names:\n')
    name1.append(name)
for j in name1:
    if j not in name2:
        name2.append(j)

for j in name2:
    counter = name1.count(j)
    print(j, ' = ',counter)