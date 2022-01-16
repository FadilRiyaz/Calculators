print('1.ONE DECIMAL eg.0.6')
print('2.TWO DECIMAL PLACES eg.0.47')
print('3.ONE NO. ON THE LEFT OF THE POINT  AND TWO NO. ONE THE RIGHT eg.3.14')
a=int(input('Enter Decimal unit:'))
if a == 1:
    print('Correct upto one decimal Number')
    num1=float(input('Enter Decimal Number:'))
    print('numerator =',num1*10,'denominator = 9')
elif a==2:
    num2=float(input('Enter Decimal Number:'))
    print('numerator =',num2*100-(num2*10),'denominator = 90')
    print((num2*100-num2*10)/90)
elif a==3:
    num3=float(input('Enter Decimal Number:'))
    print('numerator = ',num3*100-(num3),'denominator = 99')
    
