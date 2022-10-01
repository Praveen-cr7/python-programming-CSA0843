def pow(a,b):
    c=a**b
    return c
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
a=eval(input('enter number a:'))
b=eval(input('enter number b:'))
choice=eval(input('enter the operation pow/add/sub/mul/div:'))
if (choice==pow):
    o=pow(a,b)
    print(o)
elif(choice==add):
        o=add(a,b)
        print(o)
elif (choice==sub):
        o=sub(a,b)
        print(o)
elif(choice==mul):
        o=mul(a,b)
        print(o)
elif(choice==div):
        o=div(a,b)
        print(o)
else:
    print('no operation')
