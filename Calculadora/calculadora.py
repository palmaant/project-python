# Definición de la función suma, que recibe dos parámetros a y b
def suma(a, b):
    return a + b  # Retorna la suma de a y b

# Definición de la función resta, que recibe dos parámetros a y b
def resta(a, b):
    return a - b  # Retorna la resta de a y b

# Definición de la función multiplicación, que recibe dos parámetros a y b
def multiplicacion(a, b):
    return a * b  # Retorna el producto de a y b

# Definición de la función división, que recibe dos parámetros a y b
def division(a, b):
    if b != 0:  # Verifica si el divisor b no es cero
        return a / b  # Retorna el cociente de a dividido por b
    else:
        return "Error: División por cero no permitida."  # Mensaje de error si b es cero

# Definición de la función menu para mostrar las opciones al usuario
def menu():
    print("=== Calculadora ===")  # Título de la calculadora
    print("1. Suma")  # Opción para sumar
    print("2. Resta")  # Opción para restar
    print("3. Multiplicación")  # Opción para multiplicar
    print("4. División")  # Opción para dividir
    print("5. Salir")  # Opción para salir del programa

# Bucle principal para ejecutar la calculadora
while True:
    menu()  # Muestra el menú con las opciones
    opcion = input("Elige una opción: ")  # Pide al usuario que elija una opción

    # Verifica si la opción elegida es válida (1, 2, 3, o 4)
    if opcion in ["1", "2", "3", "4"]:
        try:
            # Pide al usuario ingresar dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa valores numéricos.")  # Mensaje si el usuario no ingresa números válidos
            continue  # Vuelve al inicio del bucle para intentar nuevamente

        # Ejecuta la operación correspondiente según la opción elegida
        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")  # Muestra el resultado de la suma
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")  # Muestra el resultado de la resta
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")  # Muestra el resultado de la multiplicación
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")  # Muestra el resultado de la división
    elif opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")  # Mensaje de despedida
        break  # Sale del bucle y termina el programa
    else:
        print("Opción no válida. Intenta de nuevo.")  # Mensaje si la opción ingresada no es válida
