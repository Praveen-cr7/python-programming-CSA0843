sr=int(input("enter the starting range"))
if (sr<=0):
    print("invalid")
    exit()
er=int(input("enter the ending range"))
if(er<=0):
    print("invalid entry")
    exit()
k=int(input("enter the number to be skipped"))
if(k<=0):
    print("invalid number")
    exit()
    for i  in range (sr,er,k+1):
        print("",i)
