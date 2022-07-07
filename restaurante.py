##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##
### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre: str, platos: dict,cocineros:list, repartidores: list):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0
    # metodo recibir_pedidos recibe argumento clientes que es una lista con objetos de la clase Cliente
    # recorre la lista de clientes y obtiene los platos favoritos
    #  por cada plato favorito, se le asigna un cocinero y el metodo cocinar y se le agrega a una lista llamada pedido
    # solo se le puede usar un cocienero con energia mayor a 0


    def recibir_pedidos(self, clientes: list):
        pedidos = []
        i = 0
        x = 0
        for cliente in clientes:
            for plato in cliente.platos_preferidos:   
                # este if solo verifica si la lista de cocineros no viene vacia , quizas a modo de proyecto no tenga niun sentido .
                if len(self.cocineros) > 0:
                    cocinero = self.cocineros[i]
                    if(cocinero.energia > 0):
                        pedido = cocinero.cocinar(plato)
                        pedidos.append(pedido)
                    # validar si cocinero es el ultimo en la lista y no le queda energia
                    elif(i == len(self.cocineros)-1) and (cocinero.energia <= 0):
                        print("No hay cocineros disponibles")
                        break
                    else:
                        i += 1
            # se le asigna un repartidor a cada pedido
            if len(self.repartidores) > 0 :
                repartidor = self.repartidores[x]
                if(repartidor.energia > 0):
                    repartidor.repartir(pedidos)
                    self.calificacion =+ cliente.recibir_pedido(pedidos,repartidor.tiempo_entrega)
                # validar si repartidor es el ultimo en la lista y no le queda energia
                elif(x == len(self.repartidores)-1) and (repartidor.energia <= 0):
                    self.calificacion =+ cliente.recibir_pedido([],0)
                else:
                    x += 1   
        self.calificacion = self.calificacion/len(clientes)
     
### FIN PARTE 3 #

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:

        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
