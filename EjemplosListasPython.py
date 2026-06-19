#Agregar Elementos
nombres = [] #aqui define o crea la lista

nombres.append("Ana")
nombres.append("Pedro")
nombres.append("María") #agrega un elemento tipo string especifico

print(nombres)
nombres(3,"Juan")# agrega el elemento en una pocicion especifica de la lista, en este caso seria el 3, que es la cuarta pocicion en la lista

#Búsqueda de Elementos

nombres = ["Ana","Pedro","María"]
buscar = "Juan"
if buscar in nombres:
    print("Nombre encontrado")
else:
    print("Nombre no encontrado") #utilizamos una variable para igualarla al elemento que deseamos buscar, y luego con un if-else verificamos si la variable esta dentro de la lista

#Actualización de elementos
nombres = ["Ana","Pedro","María"]
print(nombres)
nombres[1] = "Juan" #llamamos a la lista, luego entre [] se pone el indice, pocicion del elemento y se igual a lo que pretendemos actualizar
print(nombres)

#Eliminar Elementos
nombres = ["Ana","Pedro","María"]
nombres.remove("Pedro") #llamamos a la lista, luego se usa el .remove y dentro de los () se pone lo que se desea borrar
print(nombres)  #cuando el elemento no esta en la lista python devuelve un error, por lo que es recomendable usar un try except

#Ordenar elementos
nombres.reverse() #invierte el orden de la lista
nombres.sort() #ordena de menor a mayor los elementos de la lista


#Ejmeplo completo con todas las operaciones CRUD
frutas = ["Manzana", "Pera", "Naranja"]

#Agregar
nueva_fruta = input("Ingrese una Fruta")
frutas.append(nueva_fruta)

#Buscar
buscar = input("¿Qué fruta desea buscar?: ")

if buscar in frutas:
    print("La fruta Existe")
else:
    print("La fruta no existe")

#Actualizar
frutas[0] = "Platano"

#Eliminar
frutas.remove("Pera")

print("Lista Final")
print(frutas)

#Impresión de datos dentro de una Lista
libros = ["Python", "Java", "C++"]
contador = 1

#Opción 1
for libro in libros:
    print(f"{contador}. {libro}")
    contador += 1  #este blocke enumera y muestra los elementos de la lista con un numero
print("")

#Opción 2
for i, libro in enumerate(libros, start=1):
    print(i, libro) # este blocke tambien enumera, pero de una manera diferente

