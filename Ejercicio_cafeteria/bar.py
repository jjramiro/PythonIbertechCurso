import logging

from clases_bar import Client, Waiter, TooColdTemperatureException, TooHotTemperatureException

if __name__ == '__main__':
    '''
        Creamos al cliente y al camarero para el ejercicio
    '''
    client = Client("Brook")
    waiter = Waiter("Sanji")
    try:
        # el camarero ejecuta la funcion de servir la taza de cafe mandandole un cliente
        waiter.serve_coffee_cup(client)
    except TooColdTemperatureException as e:
        # lanzamos la excepcion de que el cafe esta muy frio
        logging.error(e)
    except TooHotTemperatureException as e:
        # lanzamos la excepcion de que el cafe esta muy caliente
        logging.error(e)
