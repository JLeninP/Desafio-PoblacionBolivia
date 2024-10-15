import sys
import math
def interpLagrange(X, Y, xk):
    res = 0
    n = len(X)
    L = [1]*(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i] *= (xk - X[j])/(X[i] - X[j]) 
        res += Y[i] * L[i]
    return res

def error(X, xk, yk):
    E = 1
    n = len(X)
    L = 1
    for j in range(n):
        L *= (xk - X[j])/(xk - X[j]) 
    for j in range(n):
        E *= L/ math.factorial(n+1) * (xk - X[j])
    return L

file: object = open("datos.in", "r")

X1: list[float] = list(map(float, file.readline().split()))
Y1: list[float] = list(map(float, file.readline().split()))

X2: list[float] = list(map(float, file.readline().split()))
Y2: list[float] = list(map(float, file.readline().split()))

xk: int = int(file.readline())
vR: int = int(file.readline())

yk1: float = interpLagrange(X1, Y1, xk)
yk2: float = interpLagrange(X2, Y2, xk)

Er1: float = abs(vR - yk1)/vR
Er2: float = abs(vR - yk2)/vR

sys.stdout.write(f'\n==================SOLUCIÓN LAGRANGE==================\n')

sys.stdout.write(f'\nAño: {str(xk)}\n')
sys.stdout.write(f'\nPoblación1: {yk1}')
sys.stdout.write(f'\nError1: {Er1}\n')
sys.stdout.write(f'\nPoblación2: {yk2}')
sys.stdout.write(f'\nError2: {Er2}\n')

sys.stdout.write(f'\n====================FIN PROGRAMA====================\n')
