def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE CALIFICACIONES ---")
    print("1. Ver todas las calificaciones")
    print("2. Consultar calificación por índice (estudiante)")
    print("3. Ver estadísticas (Promedio, Máxima, Mínima, Aprobados/Reprobados)")
    print("4. Modificar la calificación de un estudiante")
    print("5. Salir")

def main():
    calificaciones = [85, 67, 92, 74, 58]
    estudiantes = ["Estudiante 0", "Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4"]

    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            print("\n--- LISTA DE CALIFICACIONES ---")
            for i in range(len(calificaciones)):
                print(f"Índice [{i}] - {estudiantes[i]}: {calificaciones[i]}")

        elif opcion == "2":
            print("\n--- CONSULTAR POR ÍNDICE ---")
            try:
                idx = int(input("Ingrese el índice a consultar (0 a 4): "))
                print(f"El {estudiantes[idx]} tiene una calificación de: {calificaciones[idx]}")
            except IndexError:
                print("Error: El índice ingresado no existe en el vector.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")

        elif opcion == "3":
            print("\n--- RESUMEN ESTADÍSTICO ---")
            suma = 0
            aprobados = 0
            reprobados = 0
            
            nota_maxima = calificaciones[0]
            nota_minima = calificaciones[0]

            for nota in calificaciones:
                suma += nota
                
                if nota >= 70:
                    aprobados += 1
                else:
                    reprobados += 1

                if nota > nota_maxima:
                    nota_maxima = nota
                if nota < nota_minima:
                    nota_minima = nota

            promedio = suma / len(calificaciones)

            print(f"Promedio general: {promedio:.2f}")
            print(f"Calificación más alta: {nota_maxima}")
            print(f"Calificación más baja: {nota_minima}")
            print(f"Cantidad de estudiantes aprobados (>=70): {aprobados}")
            print(f"Cantidad de estudiantes reprobados (<70): {reprobados}")

        elif opcion == "4":
            print("\n--- MODIFICAR CALIFICACIÓN ---")
            try:
                idx = int(input("Ingrese el índice del estudiante a modificar (0 a 4): "))
                if 0 <= idx < len(calificaciones):
                    print(f"Calificación actual de {estudiantes[idx]}: {calificaciones[idx]}")
                    nueva_nota = float(input("Ingrese la nueva calificación (0-100): "))
                    
                    calificaciones[idx] = nueva_nota
                    print(f"¡Calificación actualizada con éxito! Nuevo valor: {calificaciones[idx]}")
                else:
                    print("Error: Índice fuera de rango.")
            except ValueError:
                print("Error: Entrada inválida. Ingrese un número válido.")

        elif opcion == "5":
            print("\nSaliendo del programa... ¡Hasta luego!")
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()