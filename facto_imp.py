import time

def factorial_imperativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Medición del tiempo de ejecución
n = 10000
inicio = time.time()
factorial_imperativo(n)
fin = time.time()
print(f"Tiempo de ejecución imperativo: {fin - inicio} segundos")


def factorial_declarativo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_declarativo(n - 1)

# Medición del tiempo de ejecución
inicio = time.time()
factorial_declarativo(n)
fin = time.time()
print(f"Tiempo de ejecución declarativo: {fin - inicio} segundos")


n = 10000

# Medición del tiempo para el enfoque imperativo
inicio_imperativo = time.time()
factorial_imperativo(n)
fin_imperativo = time.time()
tiempo_imperativo = fin_imperativo - inicio_imperativo

# Medición del tiempo para el enfoque declarativo
inicio_declarativo = time.time()
factorial_declarativo(n)
fin_declarativo = time.time()
tiempo_declarativo = fin_declarativo - inicio_declarativo

print(f"Tiempo de ejecución imperativo: {tiempo_imperativo} segundos")
print(f"Tiempo de ejecución declarativo: {tiempo_declarativo} segundos")




