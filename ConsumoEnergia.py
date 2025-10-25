
consumo_mensual = float(input('Ingrese el consumo mensual (kWh): '))

categoria = ""
precio_por_kwh = 0
total_a_pagar = 0
recomendacion = ""

if consumo_mensual >= 0 and consumo_mensual <= 100:
    categoria = "Bajo"
    precio_por_kwh = 450
    recomendacion = "Excelente ahorro energético"
elif consumo_mensual > 100 and consumo_mensual <= 200:
    categoria = "Medio"
    precio_por_kwh = 500
    recomendacion = "Consumo normal"
elif consumo_mensual > 200 and consumo_mensual <= 350:
    categoria = "Alto"
    precio_por_kwh = 650
    recomendacion = "Considere reducir el uso de electrodomésticos"
elif consumo_mensual > 350:
    categoria = "Crítico"
    precio_por_kwh = 800
    recomendacion = "Alerta: Consumo excesivo. Revise fugas o desconecte equipos"
else:
    categoria = "Inválido"
    recomendacion = "El consumo ingresado no es válido"

if categoria != "Inválido":
    total_a_pagar = consumo_mensual * precio_por_kwh

print("\nRESULTADOS\n")
print(f"Categoría: {categoria}")

if categoria != "Inválido":
    print("Total a pagar: $" + str(total_a_pagar))
else:
    print("Total a pagar: $0")


