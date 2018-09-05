#Calculator
#Jadam

 

repeat = True

def doMath( a,b,c ):
    if (c == 1):
        return str (a+b)
    if (c == 2):
        return str (a-b)
    if (c == 3):
        return str (a*b)
    if (c == 4):
        if (b == 0):
            return("undefined")
        return str (round(a/b,2))
    if (c == 5):
        if (b == 0):
            return("undefined")
        return str (a%b)

while repeat:
    a = int(input("This is a number: "))

    b = int(input("Indeed, this is also a number: "))
    print("Sum:\t\t" + doMath(a,b,1))
    print("Difference:\t" + doMath(a,b,2))
    print("Product:\t" + doMath(a,b,3))
    print("Quotient:\t" + doMath(a,b,4))
    print("Modulo:\t\t" + doMath(a,b,5))

    if input("repeat")=="no":
        repeat = False
