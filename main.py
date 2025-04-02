# Proyecto: [C10_Python]
# Estudiante: [Jafet Rojas]
# Fecha de Inicio: [26/03/2025]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos.carga_datos import generar_lista_compras
from analisis_datos.estadisticas import media

#from analisis_datos import *

lista_compra = generar_lista_compras()
print(lista_compra)
precios = [precio for _,precio in lista_compra]
print(precios)


#media
#paso 1: ordenar los valores ascendente
precios_asc = sorted(precios)

#cantidad
n = len(precios_asc)
print(n)
mitad = n // 2
print(mitad)
