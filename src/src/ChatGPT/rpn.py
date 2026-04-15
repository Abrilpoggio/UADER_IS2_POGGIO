# --------------------------------------------------------------------
# Evaluador de expresiones en notación polaca inversa (RPN).
# Permite números, operadores básicos, funciones matemáticas,
# comandos de pila y manejo de memoria.
# --------------------------------------------------------------------

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para errores de evaluación en RPN."""

    pass


def evaluar(expr):
    """
    Evaluar una expresión en notación polaca inversa (RPN).

    Parámetros:
        expr (str): expresión en formato RPN

    Retorna:
        float: resultado de la evaluación
    """

    # Pila de operandos
    pila = []

    # Memoria (10 posiciones)
    memoria = [0.0] * 10

    # Operadores binarios básicos
    operadores = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: (
            a / b if b != 0 else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
    }

    # Funciones de un argumento
    funciones = {
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "ex": math.exp,
        "10x": lambda x: 10**x,
        "1/x": lambda x: (
            1 / x if x != 0 else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
        "chs": lambda x: -x,
    }

    # Funciones trigonométricas (trabajan en grados)
    trigonometria = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tg": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atg": lambda x: math.degrees(math.atan(x)),
    }

    # Constantes matemáticas
    constantes = {
        "p": math.pi,
        "e": math.e,
        "j": (1 + math.sqrt(5)) / 2,
    }

    # Procesamiento de la expresión token por token
    for token in expr.split():

        # Intentar convertir a número
        try:
            pila.append(float(token))
            continue
        except ValueError:
            pass

        # Verificar si es una constante
        if token in constantes:
            pila.append(constantes[token])

        # Operadores binarios
        elif token in operadores:
            if len(pila) < 2:
                raise RPNError("Pila insuficiente")

            b = pila.pop()
            a = pila.pop()
            pila.append(operadores[token](a, b))

        # Potencia
        elif token == "yx":
            if len(pila) < 2:
                raise RPNError("Pila insuficiente")

            b = pila.pop()
            a = pila.pop()
            pila.append(a**b)

        # Funciones de un argumento
        elif token in funciones:
            if not pila:
                raise RPNError("Pila vacía")

            pila.append(funciones[token](pila.pop()))

        # Funciones trigonométricas
        elif token in trigonometria:
            if not pila:
                raise RPNError("Pila vacía")

            pila.append(trigonometria[token](pila.pop()))

        # Duplicar último valor
        elif token == "dup":
            if not pila:
                raise RPNError("Pila vacía")

            pila.append(pila[-1])

        # Intercambiar últimos dos valores
        elif token == "swap":
            if len(pila) < 2:
                raise RPNError("Pila insuficiente")

            pila[-1], pila[-2] = pila[-2], pila[-1]

        # Eliminar último valor
        elif token == "drop":
            if not pila:
                raise RPNError("Pila vacía")

            pila.pop()

        # Vaciar la pila
        elif token == "clear":
            pila.clear()

        # Guardar en memoria (STO0 a STO9)
        elif token.startswith("STO"):
            indice = int(token[3:])

            if not 0 <= indice <= 9 or not pila:
                raise RPNError("Error memoria")

            memoria[indice] = pila[-1]

        # Recuperar de memoria (RCL0 a RCL9)
        elif token.startswith("RCL"):
            indice = int(token[3:])

            if not 0 <= indice <= 9:
                raise RPNError("Error memoria")

            pila.append(memoria[indice])

        # Token inválido
        else:
            raise RPNError(f"Token inválido: {token}")

    # Validar resultado final
    if len(pila) != 1:
        raise RPNError("Resultado inválido")

    return pila[0]


def main():
    """
    Programa principal:
    Lee una expresión RPN desde la línea de comandos o por input
    y muestra el resultado.
    """
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("RPN: ")
        print(evaluar(expr))

    except RPNError as error:
        print("Error:", error)


# Ejecutar solo si es programa principal
if __name__ == "__main__":
    main()
