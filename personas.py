##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre: str, tiempo_entrega: int):
        super().__init__(nombre)
        # tiempo de entrega aleatorio entre 20 y 30
        self.tiempo_entrega = tiempo_entrega
        # energia aleatorio entre 75 y 100
        self.energia = randint(75, 100)
    # metodo repartir que recibe como parametro una lsita de platos
    def repartir(self, pedido: list):
    # disminiuya la energia del repartidor segun numero de pedido , si el numero de pedido es mayor o igual a 3 variable factor_tamano es igual a 15 sino es 5
        factor_tamano = 15 if len(pedido) >= 3 else 5
        # disminuye la energia del repartidor segun el factor de tamano
        self.energia -= factor_tamano
    # calcular el tiempo de entrega segun numero de pedido, si el numero de pedido es mayor o igual a 3 variable factor_velocidad es igual a 0.85 sino es 1.25
        factor_velocidad = 0.85 if len(pedido) >= 3 else 1.25
        # calcular el tiempo de entrega segun el factor de velocidad
        self.tiempo_entrega = self.tiempo_entrega * factor_velocidad
        # imprime el nombre del repartidor y el tiempo de entrega y energia
        print(f"El repartidor {self.nombre} se ha demorado {self.tiempo_entrega} perdiendo {self.energia} energia.")
        # retorna tiempo de entrega
        return self.tiempo_entrega

### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre: str, habilidad: int):
        super().__init__(nombre)
        # tiempo de cocina aleatorio entre 1 y 10
        self.habilidad= habilidad
        # energia aleatorio entre 50 y 80
        self.energia = randint(50, 80)
    # metodo cocinar que recibe como parametro una lista de informacion_plato que contiene el nombre del plato y el tipo de plato que puede ser comestible o bebestible
    def cocinar(self, informacion_plato: list):
    # si el tipo de plato es comestible
        if informacion_plato[1] == "Comestible":
            # crea un objeto de tipo comestible
            plato = Comestible(informacion_plato[0])
            # disminuie la energia del cocinero en 15
            self.energia -= 15
        # si el tipo de plato es bebestible
        elif informacion_plato[1] == "Bebestible":
            # crea un objeto de tipo bebestible
            plato = Bebestible(informacion_plato[0])
            # disminuie la energia del cocinero segun el tamano del plato , si el plato es Pequeño es igual a 5 si es mediano es igual a 8 si es grande es igual a 10
            self.energia -= 5 if plato.tamano == "Pequeño" else (8 if plato.tamano == "Mediano" else 10)
        # calidad del plato debe ser calculado por le factor_calidad por calidad del plato, y factor_calidad si la dificultad del plato es mayor a la habilidad del cocinero es igual a 0.7 sino 1.5
        factor_calidad =  (0.7 if plato.dificultad > self.habilidad else 1.5)
        # calcular la calidad del plato segun el factor de calidad
        plato.calidad = plato.calidad * factor_calidad
        # imprime el nombre del cocinero el plato  y la energia
        print(f"El cocinero {self.nombre} ha cocinado {plato.nombre} y perdiendo {self.energia} de energia.")
        # retorna el plato
        return plato   
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    # definir un __int __ agregar un atributo de tipo lista que contenga una lista de platos de platos_favoritos
    def __init__(self, nombre: str, platos_favoritos: list):
        super().__init__(nombre)
        # lista de platos favoritos agrega 3 platos aleatorios
        self.platos_preferidos = platos_favoritos
        # metodo recibir_pedido con 2 argumentos que recibe una lista de pedidos objeto Comestible o bebestible y una vareiable de tipo int que representa el tiempo de demora
    def recibir_pedido(self, pedido: list, demora: int):
            # se define varible calificacion que comienza en 10 y disminuye a mitad si la cantidad de platos en el pedido es menor a platos_preferidos o si la demora es mayor o igual a 20
            calificacion = 10
            if len(pedido) < len(self.platos_preferidos) or demora >= 20:
                calificacion = 5
            # luego cliente cambia calificacion dependiendo la calidad de cada plato del pedido, si la calidad es mayor o igual a 11 se le suma 1.5 a calificacion, si la calidad es menor o igual a 8 se le resta 3 a calificacion
            for plato in pedido:
                if plato.calidad >= 11:
                    calificacion += 1.5
                elif plato.calidad <= 8:
                    calificacion -= 3
            # imprime el nombre del cliente y la calificacion y pedido
            print(f"El cliente {self.nombre} ha recibido su pedido y le puso la calificacion {calificacion} ")
            # retorna la calificacion
            return calificacion

### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
