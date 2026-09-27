"""
Calculadora en Python
Operaciones básicas, potencias, raíces, logaritmos, trigonometría y más
"""

import math


# ---------- Operaciones de dos números ----------

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def potencia(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con cero")
    return a % b


def porcentaje(a, b):
    """Calcula el a% de b."""
    return a * b / 100


def raiz_n(a, n):
    """Raíz n-ésima de a."""
    if n == 0:
        raise ValueError("El índice de la raíz no puede ser cero")
    if a < 0:
        if n == int(n) and int(n) % 2 == 1:
            return -((-a) ** (1 / n))
        raise ValueError("No existe raíz par de un número negativo")
    return a ** (1 / n)


def logaritmo_base(x, base):
    if x <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos")
    if base <= 0 or base == 1:
        raise ValueError("La base debe ser positiva y distinta de 1")
    return math.log(x, base)


# ---------- Operaciones de un número ----------

def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("No existe raíz cuadrada de un número negativo")
    return math.sqrt(x)


def logaritmo_natural(x):
    if x <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos")
    return math.log(x)


def logaritmo_10(x):
    if x <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos")
    return math.log10(x)


def logaritmo_2(x):
    if x <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos")
    return math.log2(x)


def exponencial(x):
    return math.exp(x)


def factorial(x):
    if x < 0 or x != int(x):
        raise ValueError("El factorial solo está definido para enteros no negativos")
    return math.factorial(int(x))


def seno(grados):
    return math.sin(math.radians(grados))


def coseno(grados):
    return math.cos(math.radians(grados))


def tangente(grados):
    if math.isclose(math.cos(math.radians(grados)), 0, abs_tol=1e-12):
        raise ValueError("La tangente no está definida para ese ángulo")
    return math.tan(math.radians(grados))


def valor_absoluto(x):
    return abs(x)


def inverso(x):
    if x == 0:
        raise ValueError("El cero no tiene inverso")
    return 1 / x


# ---------- Menú ----------

# opción: (nombre, función, formato del resultado)
OPERACIONES_DOS = {
    "1": ("Sumar", sumar, "{a} + {b}"),
    "2": ("Restar", restar, "{a} - {b}"),
    "3": ("Multiplicar", multiplicar, "{a} * {b}"),
    "4": ("Dividir", dividir, "{a} / {b}"),
    "5": ("Potencia (a^b)", potencia, "{a} ^ {b}"),
    "6": ("Módulo / residuo (a % b)", modulo, "{a} % {b}"),
    "7": ("Porcentaje (a% de b)", porcentaje, "{a}% de {b}"),
    "8": ("Raíz n-ésima", raiz_n, "raíz {b} de {a}"),
    "9": ("Logaritmo en base personalizada", logaritmo_base, "log_{b}({a})"),
}

OPERACIONES_UNA = {
    "10": ("Raíz cuadrada", raiz_cuadrada, "√({x})"),
    "11": ("Logaritmo natural (ln)", logaritmo_natural, "ln({x})"),
    "12": ("Logaritmo base 10", logaritmo_10, "log10({x})"),
    "13": ("Logaritmo base 2", logaritmo_2, "log2({x})"),
    "14": ("Exponencial (e^x)", exponencial, "e^{x}"),
    "15": ("Factorial (x!)", factorial, "{x}!"),
    "16": ("Seno (grados)", seno, "sen({x}°)"),
    "17": ("Coseno (grados)", coseno, "cos({x}°)"),
    "18": ("Tangente (grados)", tangente, "tan({x}°)"),
    "19": ("Valor absoluto", valor_absoluto, "|{x}|"),
    "20": ("Inverso (1/x)", inverso, "1/{x}"),
}

OPCION_SALIR = "0"


def mostrar_menu():
    print("\n=== Calculadora ===")
    print("-- Operaciones con dos números --")
    for clave, (nombre, _, _) in OPERACIONES_DOS.items():
        print(f"{clave:>2}. {nombre}")
    print("-- Operaciones con un número --")
    for clave, (nombre, _, _) in OPERACIONES_UNA.items():
        print(f"{clave:>2}. {nombre}")
    print(f"{OPCION_SALIR:>2}. Salir")


def pedir_numero(mensaje):
    return float(input(mensaje))


def main():
    mostrar_menu()

    while True:
        opcion = input("\nElige una opción (0 para salir, 'm' para ver el menú): ").strip().lower()

        if opcion == OPCION_SALIR:
            print("¡Hasta luego!")
            break

        if opcion == "m":
            mostrar_menu()
            continue

        try:
            if opcion in OPERACIONES_DOS:
                nombre, funcion, formato = OPERACIONES_DOS[opcion]
                if funcion is logaritmo_base:
                    a = pedir_numero("Ingresa el número: ")
                    b = pedir_numero("Ingresa la base: ")
                elif funcion is raiz_n:
                    a = pedir_numero("Ingresa el número: ")
                    b = pedir_numero("Ingresa el índice de la raíz: ")
                else:
                    a = pedir_numero("Ingresa el primer número: ")
                    b = pedir_numero("Ingresa el segundo número: ")
                resultado = funcion(a, b)
                expresion = formato.format(a=a, b=b)
            elif opcion in OPERACIONES_UNA:
                nombre, funcion, formato = OPERACIONES_UNA[opcion]
                x = pedir_numero("Ingresa el número: ")
                resultado = funcion(x)
                expresion = formato.format(x=x)
            else:
                print("Opción no válida, intenta de nuevo.")
                continue

            print(f"Resultado: {expresion} = {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
        except OverflowError:
            print("Error: el resultado es demasiado grande")


if __name__ == "__main__":
    main()
