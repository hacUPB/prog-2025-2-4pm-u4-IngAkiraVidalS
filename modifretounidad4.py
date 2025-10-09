# --- FUNCIÓN DE SIMULACIÓN DE COMBUSTIBLE (La que ya teníamos) ---

def opcion_3_consumo_combustible():
    print("\n=== Opción 1: Simulación de Consumo de Combustible ===")
    
    # Entradas y configuración
    m_fuel = float(input("Combustible inicial (kg): "))
    m_reserva = float(input("Reserva mínima a respetar (kg): "))
    
    # DICCIONARIO DE TASAS DE CONSUMO
    TASAS_CONSUMO = {
        "1": 0.18,  # Consumo bajo (kg/min)
        "2": 0.25,  # Consumo medio (kg/min)
        "3": 0.35   # Consumo alto (kg/min)
    }

    # INICIALIZACIÓN DE VARIABLES Y LISTAS DE REGISTRO
    minutos_transcurridos = []
    registro_combustible = []
    minuto_actual = 0 
    
    # Registrar el estado inicial (Minuto 0)
    minutos_transcurridos.append(minuto_actual)
    registro_combustible.append(m_fuel)
    
    consumo_por_minuto = TASAS_CONSUMO["2"] 

    print("\nElige el nivel de potencia:")
    print("1) Bajo consumo")
    print("2) Consumo medio")
    print("3) Alto consumo")
    print("x) Salir")

    # BUCLE DE SIMULACIÓN
    while m_fuel > m_reserva:
        accion = input("Selecciona opción [1/2/3/x]: ").strip().lower()

        if accion == "x":
            print("Simulación terminada por el usuario.")
            break
        
        if accion in TASAS_CONSUMO:
            consumo_por_minuto = TASAS_CONSUMO[accion] 
        else:
            print("Opción no válida. Se asume consumo medio.")
            consumo_por_minuto = TASAS_CONSUMO["2"]
            accion = "2" 

        minuto_actual += 1
        m_fuel -= consumo_por_minuto
        
        minutos_transcurridos.append(minuto_actual)
        registro_combustible.append(m_fuel)

        if m_fuel <= m_reserva:
            print(f"\n¡Se alcanzó la reserva mínima de {m_reserva} kg!")
            break

        print(f"\nCombustible restante: {m_fuel:.1f} kg")
        print(f"Consumo por minuto: {consumo_por_minuto} kg/min")
        
    # CÁLCULO FINAL
    if accion != "x":
        tiempo_vuelo_restante = (m_fuel - m_reserva) / consumo_por_minuto
        print(f"\nTiempo de vuelo restante antes de la reserva: {tiempo_vuelo_restante:.1f} minutos")
    else:
        print("\nSimulación finalizada antes de la reserva.")

    input("\nPresiona Enter para volver al menú principal...")
    
    # Retornamos el registro y el diccionario para usarlos en la Opción 2 del menú
    return TASAS_CONSUMO, minutos_transcurridos, registro_combustible

# --- FUNCIÓN DE IMPRESIÓN LIMPIA (Nueva) ---

def imprimir_registro_limpio(tasas, minutos, combustible):
    print("\n=== Opción 2: Datos y Registro Histórico ===")
    
    # 1. IMPRIMIR DICCIONARIO (sin corchetes ni comas)
    print("\n--- Tasas de Consumo (Diccionario) ---")
    
    # Iteramos sobre los ítems del diccionario y los formateamos
    for clave, valor in tasas.items():
        if clave == "1":
            descripcion = "Bajo consumo"
        elif clave == "2":
            descripcion = "Consumo medio"
        else:
            descripcion = "Alto consumo"
            
        print(f"Opción {clave}: {descripcion} -> {valor} kg/min")

    # 2. IMPRIMIR LISTAS (sin corchetes ni comas)
    print("\n--- Historial de Minutos ---")
    
    # Convertimos la lista de números a una lista de strings para unirlos
    minutos_str = [str(m) for m in minutos]
    print("Minutos: " + " ".join(minutos_str)) # Une los elementos con un espacio

    print("\n--- Historial de Combustible (kg) ---")
    
    # Formateamos los floats y luego unimos
    combustible_str = [f"{c:.2f}" for c in combustible]
    print("Combustible: " + " ".join(combustible_str)) # Une los elementos con un espacio

    input("\nPresiona Enter para volver al menú principal...")

# --- FUNCIÓN PRINCIPAL DEL PROGRAMA (Menú) ---

def main():
    # Inicializamos las variables de registro fuera del bucle del menú
    # para que puedan ser accedidas por la Opción 2
    TASAS_CONSUMO = {"1": 0.18, "2": 0.25, "3": 0.35} # Valor inicial por si Opción 1 no se ejecuta
    MINUTOS = [0]
    COMBUSTIBLE = [0.0]
    
    while True:
        print("\n==============================================")
        print("                MENÚ PRINCIPAL                ")
        print("==============================================")
        print("1. Ejecutar Simulación de Consumo de Combustible")
        print("2. Mostrar Registro Histórico (Diccionario y Listas)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Ejecuta el problema programado y actualiza los registros
            TASAS_CONSUMO, MINUTOS, COMBUSTIBLE = opcion_3_consumo_combustible()
        
        elif opcion == "2":
            # Muestra el registro actual
            imprimir_registro_limpio(TASAS_CONSUMO, MINUTOS, COMBUSTIBLE)
            
        elif opcion == "3":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# Llama a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
