n=int(input("enter the number of elements"))
if(n<=0):
    print("invalid entry")
    exit()
arr=[]
for i in range(0,n):
    a=int(input("enter the elements "))
    arr.append(a)
enn=0
od=0
count=0
for i in range(0,n):
    if(arr[i]%2==0):
         en=en+(arr[i]*arr[i])
    else:
             od=od+(arr[i]*arr[i])
 print("sum of square of even numbers",en)
 print("sum of square of odd numbers",on)
