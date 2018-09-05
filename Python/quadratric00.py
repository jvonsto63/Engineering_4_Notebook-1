#Quadratic
#Jadam

from math import sqrt

print ("Quadratic Solver")
print ("Enter the coeeficients for ax^2 + bx +c = 0")

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

d = b**2 - 4*a*c


if d < 0:
    num_roots = 0
    print("no real roots")
elif d == 0:
    num_roots = 1
    x = ((-b) / 2*a)
    print("Root =")
    print(x)
else:
    num_roots = 2
    x1 = ((-b + sqrt(d))/(2*a))
    x2 = ((-b - sqrt(d))/(2*a))
    print("Roots =")
    print(x1,x2)





        
