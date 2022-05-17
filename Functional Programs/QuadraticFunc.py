import cmath #complex maths module
def Quadratic(a,b,c):
    
        delta= (b*b)-(4*a*c)
        root1=(-b + cmath.sqrt(delta))/(2*a)
        root2=(-b - cmath.sqrt(delta))/(2*a)
        print(root1)
        print(root2)

try:
    a=int(input('enter value of a: '))
    b=int(input('enter value of b: '))
    c=int(input('enter value of c: '))
    Quadratic(a,b,c)
except Exception as e:
    print("invalid input", e)