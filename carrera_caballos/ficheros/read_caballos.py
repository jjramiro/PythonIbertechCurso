import logging

from carrera_caballos.clases.class_caballos import Caballo
from carrera_caballos.log import logging_caballo as logs

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def readcaballos():
    list_caballos = []
    with open('ficheros/caballos.txt', 'r', encoding='utf8') as rfile:
        for line in rfile.readlines():
            logs.info('caballo leido con exito')
            string_line = line.split('|')
            caballo = Caballo(None, string_line[0], string_line[1], string_line[2], string_line[3],
                              string_line[4], string_line[5].split('\n')[0])
            list_caballos.append(caballo)
        logs.info(list_caballos)
    return list_caballos


if __name__ == '__main__':
    readcaballos()