import time

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
