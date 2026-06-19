#Validaciones

def validar_curso(nombre_curso):
    return nombre_curso.strip() != ""

def validacion_codigo(codigo):
    return codigo.strip() != ""

def existe_curso(lista_cursos, codigo):    #en los parametros de esta funcion estan la lista y la variable codigo
    for i in lista_cursos:                 #Aquí el for recorre mediante i cada elemento dentro de la lista cursos, i pasa a representar cada diccionario dentro de la lista
        if i["codigo"]==codigo:      #luego el if compara mediante i["codigo"](comando que devuelve el valor de la clave "codigo") si esque el codigo ingresado es igual a algun codigo dentro de la misma lista.
            return i                 #¿que pasa al devolver i? podemos usar i, que es el diccionario(curso en este caso) que coincide con el que estamos buscando, para mostrar o acceder a las claves:valor del diccionario en cuestion
    return None                      #al devolver none, podemos manipular el uso de esta variable para finalmente definir si ESTÁ O NO el codigo dentro de la lista usando "if funcion is none"=no xiste o "if funcion is not none"=existe

#opciones

def mostrar_menu():
    print("===== SISTEMA DE CURSOS =====")
    print("1.   Registrar curso")
    print("2.   Mostrar cursos")
    print("3.   Buscar curso")
    print("4.   Actualizar curso")
    print("5.   Eliminar curso")
    print("6.   Reporte general")
    print("7.   Salir")

def registrar_curso(lista_cursos): #OPCION 1

    codigo=input("Ingrese el código del curso: ").strip()
    if not validacion_codigo(codigo):
        print("EL código no debe estar vacío.")
        return
    if existe_curso(curso, codigo) is not None:
        print("Error: El código del curso ya existe.")
        return
    
    nombre_curso=input("Ingrese el nombre del curso: ").strip()
    if not validar_curso(nombre_curso):
        print("Error: el nombre del curso no debe estar vacío.")
        return
    
    cupos=int(input("Ingrese la cantidad de cupos disponibles del curso: "))
    try:
        if cupos<0:
            print("Error: cantidad inválida.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    valor_curso=int(input("Ingrese el valor del curso: "))
    try:
        if valor_curso<0:
            print("Error: cantidad inválida.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    
    estado="Diponible"

    curso={"codigo":codigo,
            "nombre":nombre_curso,
            "cupos":cupos,
            "valor":valor_curso,
            "estado":estado}
    
    lista_cursos.append(curso)

    print("Registro exitoso.")

def mostrar_curso(lista_cursos):                  #OPCION 2
    print("===== LISTADO DE CURSOS =====")
    if len(lista_cursos)==0:                          #si la cantidad de elementos dentro de la lista (cursos) es igual a 0, pues no hay cursos registrados
        print("No existen cursos registrados.")
        return
    for i in lista_cursos:                       #para cada indice dentro de mi lista cursos haz lo siguiente, entonces i empieza a recorrer los elementos dentro de la lista
        print("Código:  ", i["codigo"])    #un print con lo que queremos mostrar
        print("Nombre:  ", i["nombre"])    #luego al usar i["codigo"], i representa el curso(que es un diccionario), buscamos la clave ["codigo"] y nos devuelve el valor de esa clave.
        print("Cupos:  ", i["cupos"])      #por lo que printeamos el valor de esa clave.
        print("Valor:  ", i["valor"])
        print("Estado:  ", i["estado"])

def buscar_curso(lista_cursos):       #OPCION 3
    codigo=input("Ingrese el código del curso que desea buscar: ")
    if not validacion_codigo(codigo):
        print("Error este campo no debe estar vaío")
        return
    
    if existe_curso(i, codigo) is None: 
        print("Error: El código ingresado no existe")
        return
    if existe_curso(i, codigo) is not None:
        for i in codigo:
         print("Código:  ", i["codigo"])
         print("nombre:  ", i["nombre"])
         print("Cupos:  ", i["cupos"])
         print("Valor:  ", i["valor"])
         print("Estado:  ", i["estado"])

def actualizar_curso(codigo):     #OPCION 4
    codigo=input("Ingrese el código del curso que desea actualizar: ")
