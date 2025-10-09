def opcion_3_consumo_combustible():
    print("\n=== SIMULACIÓN DE CONSUMO DE COMBUSTIBLE ===")
    
    # Validación de entrada para combustible inicial
    while True:
        try:
            m_fuel = float(input("Combustible inicial (kg): "))
            if m_fuel <= 0:
                print("Error: El combustible debe ser mayor a 0 kg")
                continue
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido")
    
    # Validación de entrada para reserva
    while True:
        try:
            m_reserva = float(input("Reserva mínima a respetar (kg): "))
            if m_reserva < 0:
                print("Error: La reserva no puede ser negativa")
                continue
            if m_reserva >= m_fuel:
                print("Error: La reserva debe ser menor al combustible inicial")
                continue
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido")

    Tasas_consumo = {
        "1": 0.18,
        "2": 0.25,
        "3": 0.35
    }

    # Listas para registrar datos
    minutos_transcurridos = []
    registro_combustible = []
    registro_consumo = []  # Nueva lista para registrar el consumo usado en cada minuto
    minuto_actual = 0
    consumo_por_minuto = Tasas_consumo["2"]
    combustible_inicial = m_fuel  # Guardar valor inicial para cálculos

    print(f"\nCombustible inicial: {m_fuel:.2f} kg | Reserva: {m_reserva:.2f} kg")
    print("\nElige el nivel de potencia:")
    print("1: Consumo bajo (0.18 kg/min)")
    print("2: Consumo medio (0.25 kg/min)")
    print("3: Consumo alto (0.35 kg/min)")
    print("x: Terminar simulación")

    # Bucle principal de simulación
    while m_fuel > m_reserva:
        print(f"\n--- Minuto {minuto_actual} ---" if minuto_actual > 0 else "\n--- Inicio ---")
        print(f"Combustible actual: {m_fuel:.2f} kg")
        
        accion = input("Selecciona opción [1/2/3/x]: ").lower()
        
        if accion == "x":
            print("\nSimulación terminada por el usuario.")
            break
        
        # Determinar consumo
        consumo_anterior = consumo_por_minuto
        if accion in Tasas_consumo:
            consumo_por_minuto = Tasas_consumo[accion]
            nombres_consumo = {"1": "BAJO", "2": "MEDIO", "3": "ALTO"}
            print(f"✓ Consumo {nombres_consumo[accion]} seleccionado: {consumo_por_minuto} kg/min")
        else:
            print(" Opción no válida. Se mantiene consumo anterior.")
        
        # Verificar si el consumo agotará el combustible
        if m_fuel - consumo_por_minuto <= m_reserva:
            print(f" ¡ADVERTENCIA! Con este consumo alcanzarás la reserva en el próximo minuto")
        
        # Aplicar consumo
        minuto_actual += 1
        m_fuel -= consumo_por_minuto
        
        # Registrar datos
        minutos_transcurridos.append(minuto_actual)
        registro_combustible.append(m_fuel)
        registro_consumo.append(consumo_por_minuto)
        
        print(f"Minuto {minuto_actual}: Combustible restante: {m_fuel:.2f} kg")
        
        if m_fuel <= m_reserva:
            print(f"\ ¡ALERTA! Se alcanzó la reserva mínima de {m_reserva} kg!")
            break

    # RESUMEN FINAL MEJORADO
    print(f"\n{'='*50}")
    print("           RESUMEN FINAL DE SIMULACIÓN")
    print(f"{'='*50}")
    
    print(f"• Combustible inicial: {combustible_inicial:.2f} kg")
    print(f"• Combustible final: {m_fuel:.2f} kg")
    print(f"• Reserva establecida: {m_reserva:.2f} kg")
    print(f"• Combustible consumido: {combustible_inicial - m_fuel:.2f} kg")
    print(f"• Minutos de vuelo: {minuto_actual}")
    
    # Cálculos de tiempo
    if minuto_actual > 0:
        consumo_promedio = (combustible_inicial - m_fuel) / minuto_actual
        print(f"• Consumo promedio: {consumo_promedio:.3f} kg/min")
        
        if m_fuel > m_reserva:
            tiempo_restante = (m_fuel - m_reserva) / consumo_por_minuto
            print(f"• Tiempo hasta reserva: {tiempo_restante:.1f} minutos")
    
    # REGISTRO DETALLADO
    print(f"\n{'='*30}")
    print("     REGISTRO DETALLADO")
    print(f"{'='*30}")
    print("Minuto | Consumo (kg/min) | Combustible (kg)")
    print("-" * 45)
    
    for i in range(len(minutos_transcurridos)):
        minuto = minutos_transcurridos[i]
        consumo = registro_consumo[i]
        combustible = registro_combustible[i]
        print(f"{minuto:6} | {consumo:15.2f} | {combustible:13.2f}")
    
    # Mostrar primer y último registro
    if minutos_transcurridos:
        print(f"\n• Primer minuto: {registro_combustible[0]:.2f} kg")
        print(f"• Último minuto: {registro_combustible[-1]:.2f} kg")

    input("\nPresiona Enter para volver al menú principal...")

def mostrar_instrucciones():
    print(f"\n{'?'*50}")
    print("           INSTRUCCIONES DE USO")
    print(f"{'?'*50}")
    print("1. Ingresa el combustible total disponible en kg")
    print("2. Establece una reserva de seguridad")
    print("3. En cada minuto, elige el nivel de consumo:")
    print("   • 1 = Bajo (0.18 kg/min)")
    print("   • 2 = Medio (0.25 kg/min)") 
    print("   • 3 = Alto (0.35 kg/min)")
    print("   • x = Terminar simulación")
    print("4. El sistema alertará cuando se alcance la reserva")
    print(f"{'?'*50}")
    input("Presiona Enter para continuar...")

def main():
    while True:
        print(f"\n{'='*50}")
        print("        SIMULADOR DE CONSUMO DE COMBUSTIBLE")
        print(f"{'='*50}")
        print("1. Iniciar nueva simulación")
        print("2. Ver instrucciones de uso")
        print("3. Salir del programa")
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ")
            
            if opcion == "1":
                opcion_3_consumo_combustible()
            elif opcion == "2":
                mostrar_instrucciones()
            elif opcion == "3":
                print(f"\n{'¡'*20}")
                print("   ¡Gracias por usar el simulador!")
                print("   ¡Vuelo seguro! ")
                print(f"{'¡'*20}")
                break
            else:
                print(" Opción no válida. Por favor, selecciona 1, 2 o 3.")
        except KeyboardInterrupt:
            print(f"\n\nPrograma interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n Error inesperado: {e}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()