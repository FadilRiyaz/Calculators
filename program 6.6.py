print('CI AND SI CALCULATOR')
principal=float(input("Enter principal amount:"))
rate=float(input("Enter annual rate of interest:"))
time=float(input("Enter time(in years):"))
print("1.Calculate Simple Interest")
print("2.Calculate Compund Interest")
choice=int(input("Enter your choice (1 or 2):"))
if choice==1 :     # calculate simple interest
     interest=(principal*rate*time)/100
     amount=principal+interest
     print("Simple interest:{0:16.2f}".format(interest))
     print("Amount after interest:{0:12.2f}".format(amount))
else:                # assuming that other choice is 2 only
    # calculte compound interest
    n=int(input("Number of times interest is compounded in a year:"))
    rate=rate/100
    periods=time*n
    amount=principal*pow( (1+rate/n),periods)
    interest=amount-principal
    print("Compound interest:{0:16.3f}".format(interest))
    print("Amount after interest:{0:12.3f}".format(amount))
