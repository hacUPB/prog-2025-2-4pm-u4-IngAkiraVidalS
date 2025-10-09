# modificacion del ejercicio #3 del reto pasado 
'''
# -- OPCIÓN 3: Autonomía en espera y margen de pérdida con consumo de fuel ---

def opcion_3_consumo_combustible():
    print("\n=== Opción 3: Consumo de combustible ===")
    m_fuel = float(input("Combustible inicial (kg): "))  # Combustible inicial
    m_reserva = float(input("Reserva mínima a respetar (kg): "))  # Reserva mínima de combustible
    FF_bajo = 0.18  # Consumo bajo (kg/min)
    FF_medio = 0.25  # Consumo medio (kg/min)
    FF_alto = 0.35  # Consumo alto (kg/min)

    print("\nElige el nivel de potencia:")
    print("1) Bajo consumo")
    print("2) Consumo medio")
    print("3) Alto consumo")
    print("x) Salir")

    # Bucle para simular el consumo de combustible minuto a minuto
    while m_fuel > m_reserva:
        accion = input("Selecciona opción [1/2/3/x]: ").strip().lower()

        if accion == "1":
            m_fuel -= FF_bajo  # Disminuir combustible según el consumo bajo
        elif accion == "2":
            m_fuel -= FF_medio  # Disminuir combustible según el consumo medio
        elif accion == "3":
            m_fuel -= FF_alto  # Disminuir combustible según el consumo alto
        elif accion == "x":
            print("Simulación terminada por el usuario.")
            break
        else:
            print("Opción no válida. Se asume consumo medio.")
            m_fuel -= FF_medio

        if m_fuel <= m_reserva:
            print(f"\n¡Se alcanzó la reserva mínima de {m_reserva} kg!")
            break

        print(f"\nCombustible restante: {m_fuel:.1f} kg")
        if accion == '1':
            consumo_por_minuto = FF_bajo
        elif accion == '2':
            onsumo_por_minuto = FF_medio
        else:
            consumo_por_minuto = FF_alto

        # Imprimimos el resultado con el consumo elegido
        print(f"Consumo por minuto: {consumo_por_minuto} kg/min")

    # Ahora calculamos el tiempo total de vuelo usando el consumo correspondiente
    tiempo_vuelo = (m_fuel - m_reserva) / consumo_por_minuto

    # Imprimimos el resultado
    print(f"\nTiempo total de vuelo antes de la reserva: {tiempo_vuelo:.1f} minutos")

    input("\nPresiona Enter para continuar...")
    '''