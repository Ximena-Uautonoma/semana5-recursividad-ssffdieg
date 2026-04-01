"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""
def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    total = 0
    for monto in ventas:
        total += monto
    return total


# Versión recursiva sin usar len
def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    if ventas == []:   
        return 0
    return ventas[0] + total_ventas_recursivo(ventas[1:])


# Ejemplo de uso
ventas_diarias = [100, 200, 150, 300, 250]
print("Total con ciclo:", total_ventas_ciclo(ventas_diarias))      
print("Total recursivo:", total_ventas_recursivo(ventas_diarias))  
