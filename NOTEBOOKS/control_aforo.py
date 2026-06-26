"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: __________________________________________
Fecha: ____________________

Contexto:
El Anfiteatro del Centro Nacional de la Cultura (CENAC), en Costa Rica, tiene
capacidad máxima para 700 personas.
Fuente: https://si.cultura.cr/infraestructura/anfiteatro-del-centro-nacional-de-cultura

Objetivo:
Registre los grupos que desean entrar y evite que la ocupación supere 700.

Reglas:
- Cada entrada es un grupo completo. No se permite entrada parcial.
- Escriba "fin" para terminar.
- Acepte solo enteros mayores que cero.
- Si ocupación actual + grupo <= 700, acepte el grupo.
- Si ocupación actual + grupo > 700, rechace el grupo.

Requisitos:
- Use listas para grupos aceptados y rechazados.
- Use while, for, condicionales y try-except.
- No use menú, while True, funciones propias, CSV, listas anidadas ni
  comprensiones de listas.

Después de cada grupo válido, muestre:
- Mensaje de aceptación o rechazo.
- Ocupación actual.
- Espacios disponibles.

Al finalizar, muestre:
- Grupos aceptados, grupos rechazados y personas admitidas.
- Capacidad máxima, espacios disponibles y porcentaje de ocupación.
- Grupo aceptado más pequeño y más grande, si existe alguno.
- Estado final:
  menos de 560 = disponibilidad normal,
  560 a 699 = ocupación preventiva,
  700 = capacidad completa.

Salida esperada:
Entradas: 650, 60, 50, fin

Grupo aceptado: ingresan 650 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo rechazado: no hay espacio para 60 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo aceptado: ingresan 50 personas.
Ocupación actual: 700
Espacios disponibles: 0

REPORTE FINAL
Grupos aceptados: 2
Grupos rechazados: 1
Personas admitidas: 700
Capacidad máxima: 700
Espacios disponibles: 0
Porcentaje de ocupación: 100.00%
Grupo aceptado más pequeño: 50
Grupo aceptado más grande: 650
Estado final: capacidad completa.

Otros casos para probar:
- Entradas 100, 200, 150, fin -> 450 personas, estado normal.
- Entrada 701, fin -> grupo rechazado, 0 personas admitidas.
- Entrada fin -> reporte sin grupos aceptados.
- Texto, 0 o negativos -> entrada inválida y el programa continúa.
"""


# Desarrolle su solución a partir de esta línea.
Capacidad_Maxima = 700
ocupacion_actual = 0
grupos_aceptados = []
grupos_rechazados = []

entrada = ""

while entrada != "fin":
  entrada = input("Ingrese el tamaño del grupo (o escriba 'fin'): ").strip().lower()
  if entrada != "fin":
    try:
      grupo = int(entrada)
      if grupo <= 0:
        print("Entrada inválida. Se rechazan ceros y números negatuvos.")
      else:
        if ocupacion_actual + grupo <= Capacidad_Maxima:
          ocupacion_actual += grupo
          grupos_aceptados.append(grupo)
          espacios = Capacidad_Maxima - ocupacion_actual
          print(f"Grupo aceptado. Ocupacion: {ocupacion_actual}, Espacios disponibles: {espacios}")
        else:
          grupos_rechazados.append(grupo)
          espacios = Capacidad_Maxima - ocupacion_actual
          print(f"Grupo Rechazado. Ocupacion: {ocupacion_actual}. Espacios disponbibles: {espacios}")
    except ValueError:
      print(f"Entrada inválida. Ingrese un número entero o 'fin'.")

#REPORTE FINAL
print(f"Capacidad máxima: {Capacidad_Maxima}")
print(f"Personas admitidas: {ocupacion_actual}")
print(f"Espacios disponibles: {Capacidad_Maxima - ocupacion_actual}")

#Calculo del procentajes
procentaje = (ocupacion_actual/ Capacidad_Maxima)
print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
