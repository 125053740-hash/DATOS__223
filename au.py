numeros = [10, 20, 30, 40, 50]
print(numeros[2])

numeros = [10, 20, 30, 40, 50]
numeros[2] = 100
print(numeros)  

numeros = [10, 20, 30, 40, 50]
numeros.append(60)
print(numeros)

numeros.append(60)
numeros.append(70)
print(numeros)

numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])

print(numeros[5][0])

numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)

numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros) 

numeros = [10, 20, 30, 40]

numeros = numeros + [50, 60, 70]

print(numeros)

numeros = [10, 20, 30]
numeros[len(numeros):] = [40]
print(numeros)



calificaciones = [70, 85, 90, 65]
 
calificaciones.append(95)

calificaciones.insert(2, 80)

print(calificaciones)





colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])


print(colores)


colores.append("Negro")
print(colores[-1])  # O colores[6]

numeros = [10, 20, 30, 40]

numeros.insert(2, 95)
numeros.extend([50, 67])

print(numeros)
print(numeros[2])
print(numeros[6])

print("El número 95 ocupa la posición (índice):", numeros.index(95))
print("El número 67 ocupa la posición (índice):", numeros.index(67))