import logging

from carrera_caballos.clases.class_gran_premio import GranPremio
from carrera_caballos.log import logging_caballo as logs

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def readgrandespremios():
    list_grandespremios = []
    with open('ficheros/grandes_premios.txt', 'r', encoding='utf8') as rfile:
        for line in rfile.readlines():
            logs.info('gran premio leido con exito')
            string_line = line.split('|')
            granpremio = GranPremio(None, string_line[0], string_line[1], string_line[2].split('\n')[0])
            list_grandespremios.append(granpremio)
        logs.info(list_grandespremios)
    return list_grandespremios


if __name__ == '__main__':
    readgrandespremios()