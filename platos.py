##############################################################
from random import randint, choice
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 1.1 ###
class Plato():
   def __init__(self, nombre: str):
        self.nombre = nombre
        self.calidad = 0
### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        # tamano de bebestible  se elige de forma aleatoria entre strings "Pequeno", "Mediano", "Grande"
        self.tamano = choice(["Pequeno", "Mediano", "Grande"])
        # dificultad depende del tamano si es pequeno es 3, si es mediano es 6, si es grande es 9
        self.dificultad = 3 if self.tamano == "Pequeno" else 6 if self.tamano == "Mediano" else 9
        # calidad aleatorio entre 3 y 8
        self.calidad = randint(3, 8)  
    def __str__(self):
        return f"{self.nombre} de tipo bebestible calidad {self.calidad} y dificultad {self.dificultad}."
### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible(Plato):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        # dificultad aleatoria entre 1 y 10
        self.dificultad = randint(1, 10)
        # calidad aleatorio entre 5 y 10
        self.calidad = randint(5, 10)
    def __str__(self):
        return f"{self.nombre} de tipo comestible calidad {self.calidad} y dificultad {self.dificultad}."
### FIN PARTE 1.3 ###

if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
