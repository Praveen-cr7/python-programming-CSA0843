tu=int(input("enter total users"))
if(tu<=0):
    print("value error")
su=int(input("enter the staff users"))
if (su<=0):
    print("invalid")
a=su/3
stu=tu-su-a
print("student users",stu)
