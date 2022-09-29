try:
    def rev(st):
        st="".jion(reversed(st))
        return st
    arr=str(input("enter the stringto be reversed"))
    if (arr=='!' or arr=='@' or arr=='#' or arr=='$' or arr=='%' or arr=='^' or arr=='&' or arr=='(' or arr==')' or arr '-' or arr=='+' or arr=='_' or arr=='=' or arr=='~' or arr=='`'):
        print("special char")
        print("the string reversed", end="")
        print(rev(arr))
        except(valueerroe):
            print("integer not allowed")
