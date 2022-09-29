try:
    yr=int(input("enter the year"))
    if(yr<=0):
        print("invalid entry")
        exit()
    else:
           if(yr%400==0):
               print("leap year")
        elif(yr%100==0):
            print("not a leap year")
        elif(yr%4==0):
            print("leap year")
        else:
            print("not a leap year")
            pre=yr-3
            print("leap year",pre)
except(valueError):
    print("float value")
    exit()
