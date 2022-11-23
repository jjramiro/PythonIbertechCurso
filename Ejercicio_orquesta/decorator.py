from logging_general import log

# decorador que se ejecuta antes y despues de ejecutar las funciones de play y tune de los objetos de orquesta


def orchestra_decorator(decorator_function):
    def decorator(*args):
        log.info('decorador de antes de ejecutar')
        decorator_function(*args)
        log.info("decorador de despues de ejecutar")

    return decorator
