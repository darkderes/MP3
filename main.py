##############################################################
from random import randint, sample,seed
from secrets import choice

from personas import Cocinero,Repartidor,Cliente
from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

def crear_cocineros():
    #crea 5 cocineros y los devuelve en una lista
    cocineros_list = []
    for i in range(5):
        cocineros_list.append(Cocinero(choice(NOMBRES), randint(1, 10)))
    #imprime nombre de los cocineros
    print('Lista de cocineros:')
    for cocinero in cocineros_list:
        print(cocinero.nombre)
    return cocineros_list
    #imprime nombre de los cocineros
    
def crear_repartidores():
   #crea 2 repartidores y los devuelve en una lista
    repartidores_list = []
    for i in range(2):
        repartidores_list.append(Repartidor(choice(NOMBRES), randint(1, 10))) 
    
    print('Lista de repartidores:')
    for repartidor in repartidores_list:
        print(repartidor.nombre)
    return repartidores_list
    #imprime nombre de los repartidores
   


def crear_clientes():
    #crea 5 clientes y los devuelve en una lista
    clientes_list = [] 
    for i in range(5):
         platos = sample(list(INFO_PLATOS.values()), randint(1, 5))
         clientes_list.append(Cliente(choice(NOMBRES), platos))
    #imprime nombre de los clientes
    print('Lista de clientes:')
    for cliente in clientes_list:
        print(cliente.nombre)

    return clientes_list

def crear_restaurante():
    #crea un variable repartidores y cocineros y las iguala a la funcion crear_repartidores y crear_cocineros
    repartidores = crear_repartidores()
    cocineros = crear_cocineros()
    #crea un restaurante con los parametros de nombre, platos, cocineros y repartidores
    PLATOS_RESTAURANT = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
    restaurante = Restaurante("Bon Appetit", PLATOS_RESTAURANT, cocineros, repartidores)
    return restaurante


### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    #seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
       restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
       print(
           f"La calificación final del restaurante {restaurante.nombre} "
           f"es {restaurante.calificacion}"
       )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
