F=0
C=0
K=0
while True:
    temperature=float(input('please enter the temperature:'))                
    type_tem=input('please enter type of temperature(F,C,K):') #celsius =c ,fahrenheit = f ,kelvin  = k
    conversion=input('what temperature do you want to convert?(F,C,K):')
    
    if(type_tem=='F') and (conversion=='C'):
        c=(temperature - 32) / 1.8
        print('temperature based on Celsius is:',C)
    elif (type_tem=='C') and (conversion=='F'):
        F=(temperature * 1.8) + 32
        print('temperature based on Fahrenheit is:',F)
    elif (type_tem=='F') and (conversion=='K'):
        K=((temperature + 459.67) / 1.8)      
        print('temperature based on kelvin is:',K)
    elif (type_tem=='K') and (conversion=='F'):
        F=((temperature * 1.8) - 459.67)
        print('temperature based on Fahrenheit is:',F)
    elif (type_tem=='K') and (conversion=='C'):
        c= temperature- 273.15
        print('temperature based on Celsius is:',C)
    elif (type_tem=='C') and (conversion=='K'):
        K=temperature+ 273.15
        print('temperature based on kelvin is:',K)
    else:
        print('please try agin.')
    
    
    