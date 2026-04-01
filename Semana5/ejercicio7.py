"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    """
    Retorna el ahorro total usando iteración.
    """
    total = 0
    for ahorro in ahorros:
        total += ahorro
    return total


def ahorro_total_recursivo(ahorros):
    """
    Retorna el ahorro total usando recursividad.
    """
    # Caso base: lista vacía
    if not ahorros:
        return 0
    # Caso recursivo: primer elemento + suma del resto
    return ahorros[0] + ahorro_total_recursivo(ahorros[1:])

ahorros = [100, 200, 150, 300]

print("Total con ciclo:", ahorro_total_ciclo(ahorros))
print("Total con recursividad:", ahorro_total_recursivo(ahorros))
