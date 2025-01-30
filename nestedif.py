
y=int(input("Enter the year : "))

if y%4==0:
    if y%100==0:
        if y%400==0:
            print("Its a leap year")
        else:
            print("Its not a leap year")
    else:
        print("Its a leap year")
else:
    print("Not a leap year")