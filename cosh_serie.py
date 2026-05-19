import math


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def cosh_serie(x, n_terminos=10):
    """
    Aproxima cosh(x) usando la serie de Taylor:
    cosh(x) = sum( x^(2k) / (2k)! )  para k = 0, 1, 2, ...
    """
    suma = 0.0
    for k in range(n_terminos):
        exp = 2 * k
        termino = x**exp / factorial(exp)
        suma += termino
    return suma


def mostrar_serie(x, n_terminos=10):
    print(f"cosh({x}) con {n_terminos} términos")
    print("-" * 50)

    suma = 0.0
    for k in range(n_terminos):
        exp = 2 * k
        fact = factorial(exp)
        termino = x**exp / fact
        suma += termino
        print(f"  k={k}: x^{exp} / {exp}! = {termino:.10f}  →  parcial = {suma:.10f}")

    print("-" * 50)
    print(f"  Aproximación (serie) : {suma:.10f}")
    print(f"  Valor exacto math.cosh: {math.cosh(x):.10f}")
    print(f"  Error absoluto        : {abs(math.cosh(x) - suma):.2e}")


if __name__ == "__main__":
    x = float(input("Ingresa el valor de x: "))
    n = int(input("Número de términos (ej. 10): "))
    print()
    mostrar_serie(x, n)
