import sys

def F(X: list[float], Y: list[float]) -> float:
    n = len(X)
    if n == 2:
        return (Y[-1] - Y[0]) / (X[-1] - X[0])
    
    return (F(X[1:], Y[1:]) - F(X[:-1], Y[:-1]))/(X[-1] - X[0])

def productorio(X: list[float], xk: int) -> float:
    n = len(X)
    res = 1
    for i in range(n):
        res *= xk - X[i]
    return res

def InterpNewton(X: list[float], Y: list[float], xk: int) -> float:
    n = len(X) + 1
    P = Y[0]
    for i in range(2, n):
        f = F(X[:i], Y[:i])
        P += f * productorio(X[:i - 1], xk)

    return P

file: object = open("datos.in", "r")


X1: list[float] = list(map(float, file.readline().split()))
Y1: list[float] = list(map(float, file.readline().split()))

X2: list[float] = list(map(float, file.readline().split()))
Y2: list[float] = list(map(float, file.readline().split()))

xk: int = int(file.readline())
vR: int = int(file.readline())

yk1: float = InterpNewton(X1, Y1, xk)
yk2: float = InterpNewton(X2, Y2, xk)

Er1: float = abs(vR - yk1)/vR
Er2: float = abs(vR - yk2)/vR

sys.stdout.write(f'\n==================SOLUCIÓN NEWTON==================\n')

sys.stdout.write(f'\nAño: {str(xk)}\n')
sys.stdout.write(f'\nPoblación1: {yk1}')
sys.stdout.write(f'\nError1: {Er1}\n')
sys.stdout.write(f'\nPoblación2: {yk2}')
sys.stdout.write(f'\nError2: {Er2}\n')

sys.stdout.write(f'\n====================FIN PROGRAMA====================\n')

