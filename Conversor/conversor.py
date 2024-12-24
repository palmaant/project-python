# conversor.py
# Este script permite convertir unidades entre diferentes sistemas de medida.

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """
    Convierte unidades de longitud entre metros, kilómetros, millas y pies.
    """
    conversiones = {
        "metros": 1,
        "kilometros": 1000,
        "millas": 1609.34,
        "pies": 0.3048
    }
    # Verificamos si las unidades son válidas
    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        raise ValueError("Unidad no válida para longitud.")
    
    # Convertimos primero a metros
    valor_en_metros = valor * conversiones[unidad_origen]
    # Convertimos de metros a la unidad de destino
    return valor_en_metros / conversiones[unidad_destino]

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    """
    Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
    """
    if unidad_origen == "Celsius":
        if unidad_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "Kelvin":
            return valor + 273.15
    elif unidad_origen == "Fahrenheit":
        if unidad_destino == "Celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "Kelvin":
        if unidad_destino == "Celsius":
            return valor - 273.15
        elif unidad_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
    # Si las unidades son iguales, no hay conversión
    return valor

def convertir_masa(valor, unidad_origen, unidad_destino):
    """
    Convierte unidades de masa entre kilogramos, gramos y libras.
    """
    conversiones = {
        "kilogramos": 1,
        "gramos": 1000,
        "libras": 2.20462
    }
    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        raise ValueError("Unidad no válida para masa.")
    
    # Convertimos primero a kilogramos
    valor_en_kilogramos = valor * conversiones[unidad_origen]
    # Convertimos de kilogramos a la unidad de destino
    return valor_en_kilogramos / conversiones[unidad_destino]

def main():
    """
    Función principal que guía al usuario a través del proceso de conversión.
    """
    print("Bienvenido al conversor de unidades.")
    print("1. Longitud")
    print("2. Temperatura")
    print("3. Masa")
    
    try:
        opcion = int(input("Selecciona una opción (1, 2 o 3): "))
        if opcion == 1:
            # Conversión de longitud
            print("Unidades disponibles: metros, kilometros, millas, pies")
            valor = float(input("Ingresa el valor: "))
            unidad_origen = input("Ingresa la unidad de origen: ").lower()
            unidad_destino = input("Ingresa la unidad de destino: ").lower()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            print(f"Resultado: {resultado} {unidad_destino}")
        elif opcion == 2:
            # Conversión de temperatura
            print("Unidades disponibles: Celsius, Fahrenheit, Kelvin")
            valor = float(input("Ingresa el valor: "))
            unidad_origen = input("Ingresa la unidad de origen: ").capitalize()
            unidad_destino = input("Ingresa la unidad de destino: ").capitalize()
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            print(f"Resultado: {resultado} {unidad_destino}")
        elif opcion == 3:
            # Conversión de masa
            print("Unidades disponibles: kilogramos, gramos, libras")
            valor = float(input("Ingresa el valor: "))
            unidad_origen = input("Ingresa la unidad de origen: ").lower()
            unidad_destino = input("Ingresa la unidad de destino: ").lower()
            resultado = convertir_masa(valor, unidad_origen, unidad_destino)
            print(f"Resultado: {resultado} {unidad_destino}")
        else:
            print("Opción no válida.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
