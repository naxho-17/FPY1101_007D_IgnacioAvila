import random
import statistics
import csv
#lista Trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos generados y asignados exitosamente.")

def clasificar_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos con la opcion 1.")
        return
    
    bajo = []
    medio = []
    altos = []
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            bajo.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            medio.append((trabajador, sueldo))
        else:
            altos.append((trabajador, sueldo))
    
    print("Sueldos que son menores a $800.000")
    print(f"En Total es/son: {len(bajo)}")
    for trabajador, sueldo in bajo:
        print(f"{trabajador} ${sueldo}")
    
    print("\nSueldos que estan entre $800.000 y $2.000.000")
    print(f"En Total es/son: {len(medio)}")
    for trabajador, sueldo in medio:
        print(f"{trabajador} ${sueldo}")
    
    print("\nSueldos que son superiores a $2.000.000")
    print(f"En Total es/son: {len(altos)}")
    for trabajador, sueldo in altos:
        print(f"{trabajador} ${sueldo}")
    
    total_sueldos = sum(sueldos)
    print(f"\nTotal de dinero invertido en sueldos: ${total_sueldos}")

def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar los sueldos con la opcion 1.")
        return
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldos_prom = sum(sueldos) / len(sueldos)
    media_geom = statistics.geometric_mean(sueldos)
    
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldos_prom}")
    print(f"Media geométrica: ${media_geom}")

def reporte_de_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos con la opcion 1.")
        return
    
    with open('reporte_sueldos_Trabajadores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{trabajador} - Sueldo Base: ${sueldo}  , Descuento por Salud: ${descuento_salud},   Descuento por AFP: ${descuento_afp},   Sueldo Líquido: ${sueldo_liquido}")
    
    
    print("Reporte de sueldos redondeados generado exitosamente en 'reporte_sueldos_Trabajadores.csv'.")

def mostrar_menu():
    while True:
        print("\n***** Menú *****")
        print("1. Asignar sueldos de manera aleatoria")
        print("2. Clasificar los sueldos")
        print("3. Ver estadísticas")
        print("4. Generar Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_de_sueldos()
        elif opcion == '5':
            print("Finalizando programa… ")
            print("Desarrollado por Ignacio Avila ")
            print("RUT 21.934.332-9")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
#ejecuta el menu
if __name__ == "__main__":
    mostrar_menu()

