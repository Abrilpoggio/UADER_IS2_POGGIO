import matplotlib.pyplot as plt

# Función Collatz
def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

# Listas para gráfico
numeros = []
iteraciones = []

# Calcular para 1 a 10000
for i in range(1, 10001):
    numeros.append(i)
    iteraciones.append(collatz(i))

# Graficar
plt.plot(numeros, iteraciones)
plt.xlabel("Número inicial (n)")
plt.ylabel("Iteraciones hasta converger")
plt.title("Conjetura de Collatz")
plt.show()