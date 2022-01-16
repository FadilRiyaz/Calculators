num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))
op = input("Enter Operator{+ - * / % %2}:")
result = 0
if op == '+':
    result = num1+num2
elif op == '-':
    result = num1-num2
elif op == '*':
    result = num1*num2
elif op == '/':
    result = num1/num2
elif op == '%':
    print('#Enter First No As Whole Amount ')
    result = num2/num1*100
elif op == '%2':
    print('#Enter First No As %')
    result = num1/100*num2
else:
    print("Invalid operator")
print(num1,op,num2,'=',result)    
