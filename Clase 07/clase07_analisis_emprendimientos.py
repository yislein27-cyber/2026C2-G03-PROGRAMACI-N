"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total. """
    return sum(lista_ventas)

def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la listas ventas"""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_porcentaje(total_ventas,meta): #total de ventas = total del emprendimiento
    """Calcula el procentaje de cumplimiento de la meta"""
    return total_ventas / meta * 100

def calcular_clasificacion(porcentaje_logro):
    """Clasifica la sede segun el porcentaje de cumplimiento de la meta."""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observación, no se logró la meta"
    else:
        clasificacion_emprendimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCION"

    return clasificacion_emprendimiento

def imprimir_reporte(reporte):
    print("\nREPORTE FINAL")
    print("-"*60)
    for fila in reporte:
        print(f"Emprendimiento: {fila['nombre']}".upper())
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: {fila["total"]:,.2f}")
        print(f"Promedio diario: {fila["promedio"]:,.2f}")
        print(f"Porcentaje cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Estado: {fila["estado"]:,.2f}")
        print("-"*60)
    print(f"Cantidad de emprendimientos: {len(reporte)}")

#print("Cantidad de sedes:" , len(sedes))
#print(type(sedes), "vrs", type(sedes[0]))
#print("Datos por sede:" ,sedes[0].keys())
#print("\n Primer emprendimiento:" ,sedes[0]["nombre"])

reporte =[]
provincias = set()

for emprendimiento in sedes:
    #emprendimiento = sedes[0] #extrayendo el primer emprendimiento
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

    total_emprendimiento = calcular_total(ventas)
    promedio_emprendimiento = calcular_porcentaje(total_emprendimiento,meta)
    promedio_diario = calcular_promedio(ventas)
    clasificacion = calcular_clasificacion(promedio_emprendimiento)
    
    provincias.add(emprendimiento["provincia"]) #crea la coleccion sin duplicar valores
    
    reporte.append(
        {
            "nombre": emprendimiento["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_emprendimiento,
            "promedio": promedio_diario,
            "porcentaje": promedio_emprendimiento,
            "estado": clasificacion
        }
    )
    imprimir_reporte(reporte)
    #print(reporte)
    print(provincias)
    #print("\n Emprendimiento:" ,emprendimiento["nombre"])
    #print("Total de ventas", total_emprendimiento)
    #print("Porcentaje", promedio_emprendimiento)
    #print("Promedio diario:" ,promedio_diario)
    #print("Análisis de emprendimiento:" ,clasificacion)
    
