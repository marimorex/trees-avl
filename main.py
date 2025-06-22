from models.pacient import Paciente
from materials.avl_tree import AVL
from copy import deepcopy


def read_patients(ruta_csv, arbol_avl):
    """Lee pacientes desde un archivo CSV y los inserta en el árbol AVL."""
    import csv

    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paciente = Paciente(
                dni=fila["DNI"],
                nombre=fila["Nombre"],
                sexo=fila["Sexo"],
                edad=fila["Edad"],
                diagnosticos=fila["Diagnosticos"],
                alergias=fila["Alergias"],
                fecha_ultima_visita=fila["FechaUltimaVisita"]
            )
            arbol_avl[paciente.dni] = paciente

def imprimir_resumen(arbol_avl, nombre_centro):
    print(f"\nPacientes en {nombre_centro}: {len(arbol_avl)}")
    for dni in arbol_avl:
        print(arbol_avl[dni])

def crear_base_combinada(avl1, avl2):
    """Fusiona todos los pacientes de avl1 y avl2 en un nuevo AVL combinando duplicados."""
    base_combinada = AVL()

    # Insertar todos los pacientes de avl1
    for dni in avl1:
        base_combinada[dni] = deepcopy(avl1[dni])

    # Insertar todos los pacientes de avl2, fusionando si ya existen
    for dni in avl2:
        if dni in base_combinada:
            paciente_in_alv1 = base_combinada[dni]
            paciente_existente_in_alv2 = avl2[dni]
            base_combinada[dni] = paciente_in_alv1.combinar_con(paciente_existente_in_alv2)
        else:
            base_combinada[dni] = deepcopy(avl2[dni])

    return base_combinada

from copy import deepcopy

def crear_base_comun(avl1, avl2):
    """Crea un nuevo AVL con solo los pacientes que están en ambos árboles."""
    base_comun = AVL()

    for dni in avl1:
        if dni in avl2:
            paciente1 = avl1[dni]
            paciente2 = avl2[dni]
            fusionado = paciente1.combinar_con(paciente2)
            base_comun[dni] = fusionado  # Ya es deepcopy por dentro

    return base_comun


def menu():
    """
        Muestra un menú interactivo para realizar diferentes acciones con los árboles AVL.

        Opciones:
            1. Cargar datos de pacientes.
            2. Fusionar bases de datos (base combinada).
            3. Fusionar pacientes compartidos (base común).
            4. Salir del programa.
    """
    avl_saludplus = None
    avl_vitalclinic = None
    avl_combinada = None
    avl_comun = None

    while True:
        print("\n--------------------")
        print("Menú principal:")
        print("1. Cargar datos de pacientes")
        print("2. Fusionar bases de datos (base combinada)")
        print("3. Fusionar pacientes compartidos (base común)")
        print("4. Salir")

        opcion = input("Seleccione una opción insertando su número correspondiente: ")

        if opcion == "1":
            avl_saludplus = AVL()
            avl_vitalclinic = AVL()

            print("Cargando datos de SaludPlus...")
            read_patients("data/pacientes_saludplus.csv", avl_saludplus)
            print("Datos de SaludPlus cargados.")
            imprimir_resumen(avl_saludplus, "SaludPlus")

            print("\nCargando datos de VitalClinic...")
            read_patients("data/pacientes_vitalclinic.csv", avl_vitalclinic)
            print("Datos de VitalClinic cargados.")
            imprimir_resumen(avl_vitalclinic, "VitalClinic")

            print("\n--------------------")
            print("\nDatos correctamente cargados.")
            print("\n--------------------")


        elif opcion == "2":
            if avl_saludplus is None or avl_vitalclinic is None:
                print("Primero debe cargar los datos de los pacientes.")
            else:
                avl_combinada = crear_base_combinada(avl_saludplus, avl_vitalclinic)
                print("Base combinada:")
                imprimir_resumen(avl_combinada, "SaludCombinada (Base Combinada)")

        elif opcion == "3":
            if avl_saludplus is None or avl_vitalclinic is None:
                print("Primero debe cargar los datos de los pacientes.")
            else:
                avl_comun = crear_base_comun(avl_saludplus, avl_vitalclinic)
                print("Base comun:")
                imprimir_resumen(avl_comun, "SaludComun (Base Común)")
        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Asegúrese de seleccionar correctamente.")
    return None


if __name__ == "__main__":
    menu()