#Imports

#Helper functions
def polynomial(poly,val):
    su=0
    for power,comp in enumerate(poly):
        su += comp*(val**(len(poly)-1-power))
    return su

#Functions
def Bisection_Method(poly, start, end, eps, iterations = 1):
    mid=(start+end)/2
    if (abs(polynomial(poly, mid)) < eps):
        print("Calculation took", iterations, "iterations")
        return mid
    if (polynomial(poly, start)*polynomial(poly, mid) < 0):
        return Bisection_Method(poly, start, mid, eps, iterations + 1)
    return Bisection_Method(poly, mid, end, eps, iterations + 1)

def Newton_Raphson(poly, start, end, eps, iterations = 1):
    #stub
    return

def Secant_Method(poly, start, end, eps, iterations = 1):
    #stub
    return



#Main Function
def main():
    poly=[1,0,-3]
    start, end = 1,2
    eps = 0.00001
    methods = { "1" : Bisection_Method, "2": Newton_Raphson, "3": Secant_Method}
    print("Welcome to the program!\nEnter the method of choice:")
    print("1 - Bisection, 2 - Newton Raphson, 3 - Secant")
    print("The root is:", methods[input()](poly, start, end, eps))
    return 0

main()
