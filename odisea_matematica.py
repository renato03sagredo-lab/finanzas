import math


def divisores_propios_impares(n):
    if n <= 1:
        return 0
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 1:
                count += 1
            j = n // i
            if j != i and j != n and j % 2 == 1:
                count += 1
        i += 1
    return count


def es_gauss(n):
    if n <= 1:
        return False
    cantidad = divisores_propios_impares(n)
    if cantidad == 0:
        return False
    return n % cantidad == 0


def es_borel(n):
    digitos = str(abs(n))
    pequenos = sum(1 for d in digitos if '0' <= d <= '4')
    grandes = sum(1 for d in digitos if '5' <= d <= '9')
    return pequenos <= grandes


def es_pentagonal(n):
    if n <= 0:
        return False
    disc = 1 + 24 * n
    raiz = int(math.isqrt(disc))
    if raiz * raiz != disc:
        return False
    return (1 + raiz) % 6 == 0


def leer_n():
    while True:
        try:
            n = int(input())
            if 0 < n < 1000:
                return n
        except ValueError:
            pass


def main():
    N = leer_n()
    exitos = 0
    fracasos = 0

    for i in range(1, N + 1):
        rut = input()
        numero = int(input())

        print(f"Jugador: {i} - RUT: {rut}")

        if es_gauss(numero) and es_borel(numero) and es_pentagonal(numero):
            print(f"Número {numero} SI permite desbloquear el portal")
            exitos += 1
        else:
            print(f"Número {numero} NO permite desbloquear el portal")
            fracasos += 1

    print(f"Total de jugadores que lograron desbloquear: {exitos}")
    print(f"Total de jugadores que no lograron desbloquear: {fracasos}")


main()
