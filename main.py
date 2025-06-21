from models.pacient import Paciente
from materials.avl_tree import AVL

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
    
if __name__ == "__main__":
    avl_saludplus = AVL()
    avl_vitalclinic = AVL()

    read_patients("data/pacientes_saludplus.csv", avl_saludplus) 
    read_patients("data/pacientes_vitalclinic.csv", avl_vitalclinic) 

    imprimir_resumen(avl_saludplus, "SaludPlus")
    imprimir_resumen(avl_vitalclinic, "VitalClinic")
   

