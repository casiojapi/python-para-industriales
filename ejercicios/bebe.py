import math



def fac(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def f_tol(x,t):
    n=0
    c=0
    while c==0 or c>=t:
        c+=0-(x**(2/(fac(2))))+(x**(4/(fac(4))))-(x**(6/(fac(6))))+((-1)*n)*(x**((2*n)/(fac(2*n))))
        n=n+1
    return c

def main():
    x=int(input(" Ingrese el valor de x: "))
    t=int(input(" Ingrese el valor de tolerancia: "))
    xr=(x*math.pi/180)
    valoraprox=f_tol(x,t)
    valorexacto=math.cos(xr)
    print(" El valor aproximado es de: ",valoraprox)
    print(" El valor exacto del coseno de x es: ",valorexacto) 

main()