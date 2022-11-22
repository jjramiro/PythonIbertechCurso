from orchestra_exceptions import TuneException
from logging_general import log

# funcion que nos indica si el instrumento se toca o no correctamente dependiendo si esta afinado


def utils_tuned(tuned, name):
    if tuned:
        log.info("el instrumento {} se esta tocando correctamente".format(name))
    else:
        raise TuneException("el instrumento {} no esta afinado".format(name))