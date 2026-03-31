#!/usr/bin/python3

# Programa: factorial_OOP.py
# Implementación usando Programación Orientada a Objetos

class Factorial:

    # Constructor
    def __init__(self):
        pass

    # Método para calcular factorial de un número
    def calcular(self, num):
        if num < 0:
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return fact

    # Método run(min, max)
    def run(self, minimo, maximo):
        for n in range(minimo, maximo + 1):
            print(f"{n}! = {self.calcular(n)}")


# -------------------------
# Programa principal
# -------------------------

if __name__ == "__main__":
    f = Factorial()
    f.run(1, 5)