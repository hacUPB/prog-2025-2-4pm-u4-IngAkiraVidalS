def opcion_3_consumo_combustible():
    print("\n=== Opción 3: Consumo de combustible ===")
    
    # 1. ENTRADAS Y CONFIGURACIÓN INICIAL
    m_fuel = float(input("Combustible inicial (kg): "))  # Combustible inicial
    m_reserva = float(input("Reserva mínima a respetar (kg): "))  # Reserva mínima de combustible
    
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
    
    # Inicialización del consumo por minuto (se usa el valor medio por defecto)
    consumo_por_minuto = TASAS_CONSUMO["2"] 

    print("\nElige el nivel de potencia:")
    print("1) Bajo consumo")
    print("2) Consumo medio")
    print("3) Alto consumo")
    print("x) Salir")

    # 2. BUCLE DE SIMULACIÓN
    while m_fuel > m_reserva:
        accion = input("Selecciona opción [1/2/3/x]: ").strip().lower()

        if accion == "x":
            print("Simulación terminada por el usuario.")
            break
        
        # A. Determinar el consumo usando el diccionario
        if accion in TASAS_CONSUMO:
            # Asignamos el valor numérico del diccionario a la variable de consumo
            consumo_por_minuto = TASAS_CONSUMO[accion] 
        else:
            print("Opción no válida. Se asume consumo medio.")
            # Si es inválido, usamos el valor del consumo medio ("2")
            consumo_por_minuto = TASAS_CONSUMO["2"]
            accion = "2" 

        # B. Aplicar el consumo y registrar el tiempo
        minuto_actual += 1
        m_fuel -= consumo_por_minuto
        
        # C. REGISTRAR LOS DATOS EN LAS LISTAS
        minutos_transcurridos.append(minuto_actual)
        registro_combustible.append(m_fuel)

        # D. Verificación de reserva
        if m_fuel <= m_reserva:
            print(f"\n¡Se alcanzó la reserva mínima de {m_reserva} kg!")
            break

        # E. Impresión de Resultados
        print(f"\nCombustible restante: {m_fuel:.1f} kg")
        print(f"Consumo por minuto: {consumo_por_minuto} kg/min")
        
    # 3. CÁLCULO Y RESULTADO FINAL
    
    # Solo calculamos el tiempo si la simulación no fue interrumpida por 'x'
    if accion != "x":
        tiempo_vuelo_restante = (m_fuel - m_reserva) / consumo_por_minuto
        print(f"\nTiempo de vuelo restante antes de la reserva (con consumo final de {consumo_por_minuto} kg/min): {tiempo_vuelo_restante:.1f} minutos")
        print(f"Minutos totales simulados: {minuto_actual}")
    else:
        print("\nNo se pudo calcular el tiempo restante porque la simulación fue terminada por el usuario.")

    # OPCIONAL: Mostrar el registro completo de la simulación
    print("\n--- REGISTRO HISTÓRICO DE COMBUSTIBLE ---")
    print(f"Minutos: {minutos_transcurridos}")
    print(f"Combustible (kg): {[f'{c:.2f}' for c in registro_combustible]}")

    input("\nPresiona Enter para continuar...")