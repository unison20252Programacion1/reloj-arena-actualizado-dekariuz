# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    for i in range(m):
        print(" " * i + s * ((2*m - 1)-(i*2)))
    for i in range(m-2, -1, -1):
        print(" " * i + s * (2*m - 1 - 2*i))
    pass
