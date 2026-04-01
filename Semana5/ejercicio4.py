"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contador = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            contador += 1
    return contador(5)
print("contar_pares_ciclo: ", contar_pares_ciclo(5))


def contar_pares_recursivo(n):
    pass
