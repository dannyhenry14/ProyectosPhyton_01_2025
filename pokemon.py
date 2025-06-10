import time

inventario = {
    "Charizard": 50,
    "Pikachu": 50,
    "Bulbasaur":50}


def menu ():
    print('==================================================')
    print('*****POKEMON GAME SHOP******')
    print('==================================================')
    time.sleep(1)
    print('¡Bienvenido al sistema de gestión de la tienda!')
    print('1. Ver cartas disponibles en stock.')
    print('2. Vender cartas a un entrenador.')
    print('3. Agregar nuevas cartas al inventario.')
    print('4. Salir.')

def ver_stock():
    print("\n=== Stock actual de cartas ===")  
    for carta, cantidad in inventario.items():  
        print(f"{carta}: {cantidad} cartas")  

def vender():
    carta_input = input("¿Qué carta quiere comprar el entrenador?: ")
    
    carta_encontrada = 0
    for nombre in inventario:
        if nombre.lower() == carta_input.lower():
            carta_encontrada = nombre
            break

    if carta_encontrada:
        try:
            cantidad = int(input(f"¿Cuántas cartas de {carta_encontrada} desea comprar?: "))
            if cantidad <= inventario[carta_encontrada]:
                inventario[carta_encontrada] -= cantidad
                print(f"¡Venta realizada! Quedan {inventario[carta_encontrada]} cartas de {carta_encontrada}.")
            else:
                print(f"¡No hay suficientes! Solo quedan {inventario[carta_encontrada]} cartas de {carta_encontrada}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("Esa carta no está en el inventario.")

def agregar_cartas():
    while True:
        clave = input("Ingrese la contraseña de gerente: ")
        if clave != "atrapa":
            print("BIENVENIDO SR GERENTE!")
            break
        else:
            print("Contraseña incorrecta vuelva a intentarlo.")

    carta = input("¿Qué carta desea agregar?: (escriba cancelar para volver al menu)")

    if carta.strip().lower() == "cancelar":
        print("Operación cancelada. Volviendo al menú...")
        return

    try:
        cantidad = int(input(f"¿Cuántas cartas de {carta} desea agregar?: "))
        if carta in inventario:
            inventario[carta] += cantidad
        else:
            inventario[carta] = cantidad
        print(f"Se han agregado {cantidad} cartas de {carta}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def ejecutar_programa():
    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 1:
                ver_stock()
            elif opcion == 2:
                vender()
            elif opcion == 3:
                agregar_cartas()
            elif opcion == 4:
                print("¡Gracias por usar el sistema! Hasta luego.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número del 1 al 4.")


ejecutar_programa()

