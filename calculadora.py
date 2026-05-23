"""
Módulo calculadora.

Este archivo contiene funciones independientes para realizar
las cuatro operaciones matemáticas básicas: suma, resta,
multiplicación y división.
"""


def sumar(a, b):
    """
    Devuelve la suma de dos números.

    Parámetros:
        a: primer número.
        b: segundo número.

    Retorna:
        La suma de a + b.
    """
    return a + b


def restar(a, b):
    """
    Devuelve la resta de dos números.

    Parámetros:
        a: primer número.
        b: segundo número.

    Retorna:
        La resta de a - b.
    """
    return a - b


def multiplicar(a, b):
    """
    Devuelve la multiplicación de dos números.

    Parámetros:
        a: primer número.
        b: segundo número.

    Retorna:
        El producto de a * b.
    """
    return a * b


def dividir(a, b):
    """
    Devuelve la división de dos números.

    Parámetros:
        a: dividendo.
        b: divisor.

    Retorna:
        El cociente de a / b.

    Lanza:
        ValueError: si el divisor b es igual a cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

