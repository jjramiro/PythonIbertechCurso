import logging

from carrera_caballos.clases.class_apostante import Apostante
from carrera_caballos.log import logging_caballo as logs

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def readapostantes():
    list_apostantes = []
    with open('ficheros/apostantes.txt', 'r', encoding='utf8') as rfile:
        for line in rfile.readlines():
            logs.info('apostante leido con exito')
            string_line = line.split('|')
            apostante = Apostante(None, string_line[0], string_line[1].split('\n')[0])
            list_apostantes.append(apostante)
        logs.info(list_apostantes)
    return list_apostantes


if __name__ == '__main__':
    readapostantes()
