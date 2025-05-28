
def cargar_participantes(array_nombres:list, array_notas_primer_jurado:list,array_notas_segundo_jurado:list,array_notas_tercer_jurado:list) -> bool :
    retorno = False
    
    for i in range(len(array_notas_primer_jurado)):
        print(f"CARGANDO PARTICIPANTE {i+1}")
        
        ###  VALIDACION NOMBRE  ###
        
        
        nombre_valido = False
        while not nombre_valido:
            nombre = input("Ingrese nombre del participante: ")
            if es_letra(nombre):
                nombre_valido = True
            else:
                print("ERROR\nEl nombre debe tener al menos 3 caracteres y solo contener letras y espacios")
    
        
        ###  VALIDACION NOTA JURADO 1  ###

        nota1_valida = False
        while not nota1_valida:
            texto = input("Ingrese la nota del jurado 1 (1 al 10): ")
            if es_entero_entre_1_y_10(texto):
                nota_primer_jurado = int(texto)
                nota1_valida = True
            else:
                print("ERROR\nIngrese un numero entre 1 y 10: ")


        ###  VALIDACION NOTAS SEGUNDO JURADO  ###
        
        nota2_valida = False
        while not nota2_valida:
            texto = input("Ingrese la nota del jurado 2 (1 al 10): ")
            if es_entero_entre_1_y_10(texto):
                nota_segundo_jurado = int(texto)
                nota2_valida = True
            else:
                print("ERROR\nIngrese un numero entre 1 y 10: ")

    
        
        ###  VALIDACION NOTAS TERCER JURADO  ###

        nota3_valida = False
        while not nota3_valida:
            texto = input("Ingrese la nota del jurado 3 (1 al 10): ")
            if es_entero_entre_1_y_10(texto):
                nota_tercer_jurado = int(texto)
                nota3_valida = True
            else:
                print("ERROR\nIngrese un numero entre 1 y 10: ")

    



        array_nombres[i] = nombre
        array_notas_primer_jurado[i] = nota_primer_jurado
        array_notas_segundo_jurado[i] = nota_segundo_jurado
        array_notas_tercer_jurado[i] = nota_tercer_jurado
        
        print("PARTICIPANTE CARGADO")
        
        retorno = True
        
    return retorno


def es_letra(nombre:str) -> bool:
    if len(nombre) < 3:
        return False
    
    valido = True
    for i in range(len(nombre)):
        valor_ascii = ord(nombre[i])
        if valor_ascii > 122 or valor_ascii < 97 and valor_ascii > 90 or valor_ascii < 65 and valor_ascii != 32:
            valido = False
            break
    
    return valido


def mostrar_puntuaciones(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado):
    for i in range(len(array_nombres)):

   ### Muestra las puntuaciones de todos los participantes, incluyendo las notas de cada jurado y el promedio general de cada uno.

   ### Parámetros:
   ### - array_nombres (list): Lista de nombres de los participantes.
   ### - array_notas_primer_jurado (list): Notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Notas del jurado 3.

   ### Retona: None


        promedio = (array_notas_primer_jurado[i] + array_notas_segundo_jurado[i] + array_notas_tercer_jurado[i]) / 3
        print(array_nombres[i], "- Jurado1:", array_notas_primer_jurado[i],
              ", Jurado2:", array_notas_segundo_jurado[i],
              ", Jurado3:", array_notas_tercer_jurado[i],
              ", Promedio:", promedio)


def es_entero_entre_1_y_10(texto: str) -> bool:
    if texto == '10':
        return True
    elif len(texto) == 1 and texto >= '1' and texto <='9':
            return True
    else:
        return False


def calcular_promedio(acumulador:float | int, contador:int) -> float | None:


   ### Calcula el promedio dividiendo el acumulador por el contador.
    
   ### Parámetros:
   ### - acumulador: suma de valores.
   ### - contador: cantidad de valores.

   ###Retorna:
   ###- El promedio si el contador es distinto de cero, si no, None.
    

    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio


def mostrar_promedios_menores_a_4(array_nombres:list, array_notas_primer_jurado:list, array_notas_segundo_jurado:list, array_notas_tercer_jurado:list):

   ### Muestra los participantes cuyo promedio de notas es menor a 4.

   ### Parámetros:
   ### - array_nombres (list): Lista de nombres de los participantes.
   ###  - array_notas_primer_jurado (list): Lista de notas del jurado 1. 
   ###  - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorna: None


    hay_menores = False

    for i in range(len(array_nombres)):
        acumulador = array_notas_primer_jurado[i] + array_notas_segundo_jurado[i] + array_notas_tercer_jurado[i]
        promedio = calcular_promedio(acumulador, 3)
        if promedio != None and promedio < 4:
            print(f"{array_nombres[i]} - Promedio: {promedio:.2f}")
            hay_menores = True

    if not hay_menores:
        print("No hay participantes con promedio menor a 4.")


def mostrar_promedios_menores_a_8(array_nombres:list, array_notas_primer_jurado:list, array_notas_segundo_jurado:list, array_notas_tercer_jurado:list):

   ### Muestra los participantes cuyo promedio de notas es menor a 8.

   ### Parámetros:
   ### - array_nombres (list): Lista de nombres de los participantes.
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorna: None.



    hay_menores = False

    for i in range(len(array_nombres)):
        acumulador = array_notas_primer_jurado[i] + array_notas_segundo_jurado[i] + array_notas_tercer_jurado[i]
        promedio = calcular_promedio(acumulador, 3)
        if promedio != None and promedio < 8:
            print(f"{array_nombres[i]} - Promedio: {promedio:.2f}")
            hay_menores = True

    if not hay_menores:
        print("No hay participantes con promedio menor a 8.")


def mostrar_promedio_por_jurado(array_notas_primer_jurado:list, array_notas_segundo_jurado:list, array_notas_tercer_jurado:list):

   ### Calcula y muestra el promedio de calificaciones otorgadas por cada jurado.


   ### Parámetros: 
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorna: None.

    ###  Promedio jurado 1  ###
    acumulador1 = 0
    for nota in array_notas_primer_jurado:
        acumulador1 += nota
    promedio1 = calcular_promedio(acumulador1, len(array_notas_primer_jurado))

    ###  Promedio jurado 2  ###
    acumulador2 = 0
    for nota in array_notas_segundo_jurado:
        acumulador2 += nota
    promedio2 = calcular_promedio(acumulador2, len(array_notas_segundo_jurado))

    ###  Promedio jurado 3  ###
    acumulador3 = 0
    for nota in array_notas_tercer_jurado:
        acumulador3 += nota
    promedio3 = calcular_promedio(acumulador3, len(array_notas_tercer_jurado))

    ###  MOSTRAR PROMEDIOS  ###
    print(f"Promedio Jurado 1: {promedio1:.2f}")
    print(f"Promedio Jurado 2: {promedio2:.2f}")
    print(f"Promedio Jurado 3: {promedio3:.2f}")


def jurado_mas_estricto(array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado):

   ### Determina y muestra qué jurado fue el más estricto (es decir, el que tuvo menor promedio de calificaciones).

   ### Parámetros:
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorna: None.



    acumulador1 = 0
    for nota in array_notas_primer_jurado:
        acumulador1 += nota
    promedio1 = calcular_promedio(acumulador1, len(array_notas_primer_jurado))

    acumulador2 = 0
    for nota in array_notas_segundo_jurado:
        acumulador2 += nota
    promedio2 = calcular_promedio(acumulador2, len(array_notas_segundo_jurado))

    acumulador3 = 0
    for nota in array_notas_tercer_jurado:
        acumulador3 += nota
    promedio3 = calcular_promedio(acumulador3, len(array_notas_tercer_jurado))

    min_promedio = promedio1
    jurado = "Primer jurado"

    if promedio2 < min_promedio:
        min_promedio = promedio2
        jurado = "Segundo jurado"
    if promedio3 < min_promedio:
        min_promedio = promedio3
        jurado = "Tercer jurado"

    print("El jurado más estricto es:", jurado, "con un promedio de", min_promedio)


def jurado_mas_generoso(array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado):

   ### Determina y muestra qué jurado fue el más generoso (es decir, el que tuvo mayor promedio de calificaciones).

   ### Parámetros:
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorna: None.

    acumulador1 = 0
    for nota in array_notas_primer_jurado:
        acumulador1 += nota
    promedio1 = calcular_promedio(acumulador1, len(array_notas_primer_jurado))

    acumulador2 = 0
    for nota in array_notas_segundo_jurado:
        acumulador2 += nota
    promedio2 = calcular_promedio(acumulador2, len(array_notas_segundo_jurado))

    acumulador3 = 0
    for nota in array_notas_tercer_jurado:
        acumulador3 += nota
    promedio3 = calcular_promedio(acumulador3, len(array_notas_tercer_jurado))

    max_promedio = promedio1
    jurado = "Primer jurado"

    if promedio2 > max_promedio:
        max_promedio = promedio2
        jurado = "Segundo jurado"
    if promedio3 > max_promedio:
        max_promedio = promedio3
        jurado = "Tercer jurado"

    print("El jurado más generoso es:", jurado, "con un promedio de", max_promedio)


def participantes_puntuaciones_iguales(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado):

   ### Muestra los participantes que tienen el mismo total o promedio de notas.

   ### Parámetros:
   ### - array_nombres (list): Lista de nombres de los participantes.
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2. 
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorno: None.

    encontrados = False

    for i in range(len(array_nombres)):
        total_i = array_notas_primer_jurado[i] + array_notas_segundo_jurado[i] + array_notas_tercer_jurado[i]
        promedio_i = total_i / 3

        for j in range(i + 1, len(array_nombres)):
            total_j = array_notas_primer_jurado[j] + array_notas_segundo_jurado[j] + array_notas_tercer_jurado[j]
            promedio_j = total_j / 3

            if total_i == total_j or promedio_i == promedio_j:
                print(f"{array_nombres[i]} y {array_nombres[j]} tienen el mismo total o promedio ({total_i} o {promedio_i:.2f})")
                encontrados = True

    if not encontrados:
        print("No hay participantes con el mismo total o promedio de notas.")


def buscar_participante_por_nombre(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado):

   ### Busca y muestra los datos de un participante por su nombre, incluyendo las notas y el promedio. 

   ### Parámetros: 
   ### - array_nombres (list): Lista de nombres de los participantes.
   ### - array_notas_primer_jurado (list): Lista de notas del jurado 1.
   ### - array_notas_segundo_jurado (list): Lista de notas del jurado 2.
   ### - array_notas_tercer_jurado (list): Lista de notas del jurado 3.

   ### Retorno: None.

    nombre_buscado = input("Ingrese el nombre del participante a buscar: ")
    encontrado = False

    for i in range(len(array_nombres)):
        if array_nombres[i] == nombre_buscado:
            total = array_notas_primer_jurado[i] + array_notas_segundo_jurado[i] + array_notas_tercer_jurado[i]
            promedio = total / 3
            print("Participante encontrado:")
            print("Nombre:", array_nombres[i])
            print("Jurado 1:", array_notas_primer_jurado[i])
            print("Jurado 2:", array_notas_segundo_jurado[i])
            print("Jurado 3:", array_notas_tercer_jurado[i])
            print("Promedio:", promedio)
            encontrado = True
            break

    if not encontrado:
        print("El participante no existe.")
