"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    numeros = []
    for i in range (1,n+1):
        numeros.append(i)
    return(numeros)
print(contar_ciclo(5))
#se coloco el primer item de ejercicio


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    if n == 1:
        return [1]
    else:
        return contar_recursivo(n-1)+ [n]
print(contar_recursivo(5))
    

