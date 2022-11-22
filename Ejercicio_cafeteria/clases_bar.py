import logging as log
from random import randint
from exceptions_coffee import TooHotTemperatureException, TooColdTemperatureException

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../Ejercicio_cafeteria/logs/coffee.log'),
                    log.StreamHandler()
                ])


class CoffeeCup:

    def __init__(self, temperature, coffee_type):
        self.temperature = temperature
        self.type = coffee_type


class Human:

    def __init__(self, name):
        self.name = name


class Client(Human):

    def __init__(self, name):
        Human.__init__(self, name)

    def drink_coffee_cup(self, coffee):
        '''
            funcion de tomar la taza de cafe, si la temperatura del objeto esta muy caliente o muy fria
            se lanza una excepcion y se recoge en el programa principal si no simplemente se imprime un mensaje
            de que ha ido bien
        '''
        if coffee.temperature > 80:
            raise TooHotTemperatureException('El cliente se ha quemado')
        elif coffee.temperature < 20:
            raise TooColdTemperatureException('el cafe esta demasiado frio')
        else:
            log.info("el cliente se ha ido muy feliz!")


class Waiter(Human):

    def __init__(self, name):
        Human.__init__(self, name)

    def serve_coffee_cup(self, client):
        '''
            funcion para servir la taza de cafe, se crea el objeto cafe pidiendole el tipo al usuario y para
            la temperatura se genera un entero aleatorio, despues de esto se llama a la funcion de tomar taza de cafe
            del cliente pasandole al taza de cafe
        '''
        temperature = randint(0, 100)
        coffee_type = input("Que tipo de cafe desea tomar: ")
        coffee = CoffeeCup(temperature, coffee_type)
        client.drink_coffee_cup(coffee)
