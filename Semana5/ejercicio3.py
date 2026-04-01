"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado =1
    for i in range(1,n +1):
        resultado *= i
    return resultado
    print("factorial_ciclo: ",factorial_ciclo(5))



def factorial_recursivo(n):
    pass
