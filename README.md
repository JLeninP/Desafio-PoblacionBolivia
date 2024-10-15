---
title: "Desafio Población Bolivia"
subtitle: "Interpolación de Lagrange y Newton"
author: "Lenin Pocoaca"
date: "15-10-24"
---

# Comparando la Interpolación de polinomios de Lagrange con Newton

Para esta comparación se trabajara con las poblaciones de los ultimos 7 censos realizados por el INE (_Instituto Nacional de Estadistica_) sin contar con el ultimo.

Se estimara un valor aproximado para el censo realizado el 23 de Marzo de 2024 con los métodos de interpolación de Lagrange y Newton, para luego realizar una comparación de los resultados y ver que método de interpolación tiene una mejor aproximación al valor real, es decir, el método con el menor error relativo.

|Año|Población|
|:-:|:-:|
|1900|1633910|
|1950|2704165|
|1976|4613486|
|1992|6420792|
|2001|8274325|
|2012|10027254|


## Polinomio de Interpolación de Lagrange
Este polinomio esta determinado por:

$$P(x) = f(x_0)L{n,0}(x) + \cdots + f(x_n)L_{n,n}(x)$$

donde, para cada $k=0, 1, ..., n$

$$L{n,k}(x)=\frac{(x-x_0)(x-x_1)\cdots(x-x_{k-1})(x-x_{k+1})\cdots(x_k-x_n)}{(x_k-x_0)(x_k-x_1)\cdots(x_k-x_{k-1})(x_k-x_{k+1})\cdots(x_k-x_n)}$$

 ### Solución implementada en python
 ```{python}
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

X1: list[float] = [1900, 1950, 1976, 1992, 2001, 2012]
Y1: list[float] = [1633910, 2704165, 4613486, 6420792, 8274325, 10027254]
X2: list[float] = [1992, 2001, 2012]
Y2: list[float] = [6420792, 8274325, 10027254]

xk: int = 2024
vR: int = 11312620

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
```
### Resultados
|n|$P_n(x)$|$f(x)$|$E_r$|
|:-:|:-:|:-:|:-:|
|$6$|7142362.62433029|11312620|0.36863762556063145|
|$3$|11296585.357575763|11312620|0.001417411919098934|

Tomando todos los datos de la tabla, el valor aproximado se aleja bastante del valor real, sin embargo si se toma solo los valores cercanos al punto de observación, el error disminuye considerablemente.

## Diferencias divididas de Newton

Para cada $k = 0, 1, ..., n$

$P_n(x)$ se puede reescribir en una forma llamada diferencias divididas de Newton:

$$P_n(x)=f[x_0] + \sum_{x = 1}^{n} f[x_0, x_1, ..., x_k](x - x_0)(x - x_1)\cdots(x - x_{k - 1})$$

### Solución implementada en python
```{python}
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

X1: list[float] = [1900, 1950, 1976, 1992, 2001, 2012]
Y1: list[float] = [1633910, 2704165, 4613486, 6420792, 8274325, 10027254]
X2: list[float] = [1992, 2001, 2012]
Y2: list[float] = [6420792, 8274325, 10027254]

xk: int = 2024
vR: int = 11312620

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
```
### Resultados
|n|$P_n(x)$|$f(x)$|$E_r$|
|:-:|:-:|:-:|:-:|
|$6$|7142362.624330267|11312620|0.3686376255606334|
|$3$|11296585.357575757|11312620|0.001417411919099428|

Al igual que en el método de interpolación de Lagrange, tomando todos los datos de la tabla el valor aproximado se aleja bastante del valor real, sin embargo si se toma solo los valores cercanos al punto de observación, el error tambien disminuye considerablemente.

## Comparación
Para esta comparación se tomá las interpolaciones con los tres valores cercanos al punto de observación.
|Interpolación|$P_3(x)$|$f(x)$|$E_r$|
|:-:|:-:|:-:|:-:|
|Lagrange|11296585.357575763|11312620|0.001417411919098934|
|Newton|11296585.357575757|11312620|0.001417411919099428|

Viendo la tabla de comparación se observa que la diferencia de los errores de las interpolaciones es bastante insignificante.

Asi, entonces se puede concluir que; ambos métodos generan un polinomio que se ajusta bastante bien a los datos que son cercanos al punto de observación, logrando asi una buena estimación del valor poblacional.