from Funciones import *
from Inputs import *

# Variables principales donde se guardan los datos "activos"

bandera_carga = True
opcion = ""


while opcion != "10":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Usar datos de prueba.")
    print("2. Mostrar puntuaciones (notas y promedio).")
    print("3. Mostrar participantes con promedio menor a 4.")
    print("4. Mostrar participantes con promedio menor a 8.")
    print("5. Mostrar promedios por jurado.")
    print("6. Mostrar jurado más estricto.")
    print("7. Mostrar jurado más generoso.")
    print("8. Mostrar participantes con el mismo promedio o total de nota.")
    print("9. Ingresar nombre de participante par ver datos.")
    print("10. Salir.")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        datos_nombres = [array_nombres[i] for i in range(len(array_nombres))]
        datos_notas1 = [array_notas_primer_jurado[i] for i in range(len(array_notas_primer_jurado))]
        datos_notas2 = [array_notas_segundo_jurado[i] for i in range(len(array_notas_segundo_jurado))]
        datos_notas3 = [array_notas_tercer_jurado[i] for i in range(len(array_notas_tercer_jurado))]
        bandera_carga = True
        print("Datos de prueba cargados correctamente.")

    

    elif opcion == "2":
        if bandera_carga:
            mostrar_puntuaciones(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado,array_notas_tercer_jurado)
        else:
            print("Primero debe cargar los datos (opción 1).")
    
    
    elif opcion == "3":
        if bandera_carga:
            mostrar_promedios_menores_a_4(datos_nombres, datos_notas1, datos_notas2, datos_notas3)
        else:
            print("Primero debe cargar los datos (opción 1).")

    elif opcion == "4":
        if bandera_carga:
            mostrar_promedios_menores_a_8(datos_nombres, datos_notas1, datos_notas2, datos_notas3)
        else:
            print("Primero debe cargar los datos (opción 1).")

    elif opcion == "5":
        if bandera_carga:
            mostrar_promedio_por_jurado(datos_notas1, datos_notas2, datos_notas3)
        else:
            print("Primero debe cargar los datos (opción 1).")

    elif opcion == "6":
        if bandera_carga:
            jurado_mas_estricto(array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado)
        else:
            print("Primero debe cargar los datos (opción 1).")

    elif opcion == "7":
        if bandera_carga:
            jurado_mas_generoso(array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado)
        else:
            print("Primero debe cargar los datos (opción 1).")

    elif opcion == "8":
        if bandera_carga:
            participantes_puntuaciones_iguales(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado)
        else:
            print("Primero debe cargar los datos (opción 1).")


    elif opcion == "9":
        if bandera_carga:
            buscar_participante_por_nombre(array_nombres, array_notas_primer_jurado, array_notas_segundo_jurado, array_notas_tercer_jurado)
        else:
            print("Primero debe cargar los datos (opción 1).")


    

    elif opcion == "10":
        print("¡Gracias por usar el programa! Hasta luego.")

    else:
        print("Opción no válida, por favor intente nuevamente.")
