#Declarando un arreglo bien
numeros=[10, 20, 30, 40, 50 ]

#Imprime la pos. 30
print(numeros[2])

#Reasigne el valor de la pos. 3 a 15
numeros[3]=15
print(numeros)

#Agregamos unnvalor nuevo al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos por pos.
numeros.pop(1)
print(numeros)

# Eliminamos por valor
numeros.remove(30)
print(numeros)

frutas=["manzana", "pera", "platano", "fresa"]
frutas.remove("platano")
print(frutas)

#Agregar
frutas.append("kiwi")
print(frutas)

frutas[2]="sandia"
print(frutas)

arreglo=[]
n=int(input("Ingrese el tamaño del arreglo: "))
arreglo=[0]
  