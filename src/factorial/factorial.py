#!/usr/bin/python3
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * Calcula el factorial de un número o rango                               *
# * Modificado por: Abril Poggio                                            *
# * Materia: Ingeniería de Software II                                      *
# *-------------------------------------------------------------------------*

import sys

# Función que calcula el factorial de un número
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# -------------------------
# Entrada de datos
# -------------------------

# Si no se pasa argumento, pedirlo por teclado
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango: ")
else:
    entrada = sys.argv[1]

# -------------------------
# Procesamiento
# -------------------------

# Caso: rango (ej: 4-8, -10, 5-)
if "-" in entrada:
    partes = entrada.split("-")

    # Caso "-10" → desde 1 hasta 10
    if partes[0] == "":
        desde = 1
        hasta = int(partes[1])

    # Caso "5-" → desde 5 hasta 60
    elif partes[1] == "":
        desde = int(partes[0])
        hasta = 60

    # Caso "4-8"
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

    # Calcular factoriales en el rango
    for n in range(desde, hasta + 1):
        print(f"{n}! = {factorial(n)}")

# Caso: número simple
else:
    num = int(entrada)
    print(f"Factorial {num}! es {factorial(num)}")