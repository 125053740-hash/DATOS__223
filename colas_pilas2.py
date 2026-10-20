ejecutar_de_nuevo = "s"

while ejecutar_de_nuevo.lower() == "s":
    # Inicializamos la pila como una lista vacía para cada ejecución
    pila = []
    opcion = ""

    while opcion != "4":
        
        print("\n--- MENÚ DE PILA ---")
        print("1. Insertar en pila (Push)")
        print("2. Borrar de pila (Pop)")
        print("3. Listar pila")
        print("4. Salir del menú")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            # Insertar elemento al final (arriba de la pila)
            numero = int(input("Ingresa un número: "))
            pila.append(numero)
            print("Número ingresado a la pila.")

        elif opcion == "2":
            # Eliminar el ÚLTIMO elemento ingresado
            if len(pila) > 0:
                eliminado = pila.pop()
                print("Se sacó el número del tope:", eliminado)
            else:
                print("La pila está vacía, no hay nada que borrar.")

        elif opcion == "3":
            # Mostrar los elementos de la pila
            if len(pila) > 0:
                print("Contenido de la pila (del último al primero):")
                # Mostramos los elementos en orden inverso para visualizar el tope arriba
                for elemento in reversed(pila):
                    print(elemento)
            else:
                print("La pila está vacía.")

        elif opcion == "4":
            print("Saliendo del menú actual...")

        else:
            print("Opción no válida. Intenta de nuevo.")

    
    ejecutar_de_nuevo = input("\n¿Deseas ejecutar el programa de nuevo? (s/n): ")

print("\n¡Programa finalizado!")