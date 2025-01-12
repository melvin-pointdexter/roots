#Imports

#Helper functions
def polynomial(poly,val):
    su=0
    for power,comp in enumerate(poly):
        su += comp*(val**(power))
    return su

def derivitive(poly, val):
    deriv=[poly[i] * i for i in range(1, len(poly))]
    return polynomial(deriv, val)

#Functions
def Bisection_Method(poly, start, end, eps, iterations = 1):
    mid=(start+end)/2
    if (abs(polynomial(poly, mid)) < eps):
        print("Calculation took", iterations, "iterations")
        return mid
    if (polynomial(poly, start)*polynomial(poly, mid) < 0):
        return Bisection_Method(poly, start, mid, eps, iterations + 1)
    return Bisection_Method(poly, mid, end, eps, iterations + 1)

def Newton_Raphson(poly, cur, useless, eps, iterations = 1):
    nex=cur-(polynomial(poly,cur)/derivitive(poly,cur))
    if (abs(polynomial(poly, nex)) < eps):
        print("Calculation took", iterations, "iterations")
        return nex
    return Newton_Raphson(poly, nex, useless, eps, iterations+1)

def Secant_Method(poly, cur, prev, eps, iterations = 1):
    nex=cur - polynomial(poly, cur) * ((prev-cur)/(polynomial(poly, prev) - polynomial(poly, cur)))
    if (abs(polynomial(poly, nex)) < eps):
        print("Calculation took", iterations, "iterations")
        return nex
    return Secant_Method(poly, nex, cur, eps, iterations+1)



#Main Function
def main():
    poly=[-3,0,1]
    start, end = 1,2
    eps = 0.00001
    methods = { "1" : Bisection_Method, "2": Newton_Raphson, "3": Secant_Method}
    print("Welcome to the program!\nEnter the method of choice:")
    print("1 - Bisection, 2 - Newton Raphson, 3 - Secant")
    print("The root is:", methods[input()](poly, start, end, eps))
    return 0

main()
