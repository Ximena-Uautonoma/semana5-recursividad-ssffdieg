"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *=base
    return resultado
print("La potencia en ciclo: ", potencia_ciclo(2,4))


def potencia_recursiva(base, exponente):
    if exponente == 0:
        return  1
    else:
        return base * potencia_recursiva(base, exponente -1)
print("La potencia en recursividad: ", potencia_recursiva(2,4))

