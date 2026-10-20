ejecutar_de_nuevo = "s"

while ejecutar_de_nuevo.lower() == "s":
    # Inicializamos la cola 
    cola = []
    opcion = ""

    while opcion != "4":
        
        print("\n--- MENÚ DE COLA ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir del menú")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            # Insertar elemento al final de la cola
            numero = int(input("Ingresa un número: "))
            cola.append(numero)
            print("Número ingresado correctamente.")

        elif opcion == "2":
            # Eliminar el primer elemento 
            if len(cola) > 0:
                eliminado = cola.pop(0)
                print("Se sacó el número:", eliminado)
            else:
                print("La cola está vacía, no hay nada que borrar.")

        elif opcion == "3":
            # Mostrar los elementos de la cola
            if len(cola) > 0:
                print("Contenido de la cola:")
                for elemento in cola:
                    print(elemento)
            else:
                print("La cola está vacía.")

        elif opcion == "4":
            print("Saliendo del menú actual...")

        else:
            print("Opción no válida. Intenta de nuevo.")

    # Preguntar al usuario si desea reiniciar el programa
    ejecutar_de_nuevo = input("\n¿Deseas ejecutar el programa de nuevo? (s/n): ")

print("\n¡Programa finalizado!")