print("#Minimum Marks For Passing is Greater Than 31")
num1 = float(input("Enter Marks:"))
if num1>100:
    print('Invalid Marks!')
elif num1 >= 91:
    print('Congratulations!! you have scored A+ Grade')
elif num1 >= 81:
    print('Congrats! you have scored A Grade')
elif num1 >= 71:
    print('You you have scored B+ Grade')
elif num1 >= 61:
    print('You Have scored B Grade')
elif num1 >= 51:
    print('You Have scored C+ Grade')
elif num1>=41:
    print('You Have scored E+ Grade')
elif num1>=31:
    print('You Have scored E Grade')
elif num1<0:
    print('Invalid Marks!')
else:
    print("Student Is Failed!")
