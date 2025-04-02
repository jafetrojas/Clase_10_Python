# En este módulo se crea la lista de compras.
import random

def generar_lista_compras():
    canasta_basica = {
        'arroz' : 1800,
        'azucar' : 2200,
        'harina' : 1200,
        'tomate' : 2500,
        'frijoles' : 1400,
        'papas' : 3000,
        'leche' : 1000,
        'cerveza' : 1000,
        'cafe' : 5000,
        'fideos' : 800,
        'jabón' : 1500,
        'huevos' : 3500,
        'naranjas': 2500,
        'sal' : 800
    }
    #aqui voy a selccionar aleatoriamente 5 productos de la canasta básica.
    seleccion = random.sample(list(canasta_basica.items()),k=5)
    return seleccion
    