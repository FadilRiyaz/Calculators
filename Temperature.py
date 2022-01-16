a=float(input('Enter Temperature:'))
print('Choose any number to do any operation')
print('1.Celsius to fahrenheit')
print('2.celsius to kelvin')
print('3.fahrenheit to celsius')
print('4.Fahrenheit to kelvin')
print('5.Celsius to Rankine')
print('6.Fahrenheit to Rankine')
print('7.kelvin to rankine')
print('8.kelvin to celsius')
print('9.kelvin to fahrenheit')
b=float(input('Enter Number:'))
if b==1:
    print(a*9/5+32)
elif b==2:
    print(a+273.15)
elif b==3:
    print((a-32)*5/9)
elif b==4:
    print((a-32)/1.8+273.15)
elif b==5:
    print((a*1.8)+492)
elif b==6:
    print(a+459.67)
elif b==7:
    print((a-273.15)*1.8+491.67)
elif b==8:
    print(a-273.15)
elif b==9:
    print((a-273.15)*1.8+32)

    
    
