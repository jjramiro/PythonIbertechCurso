from carrera_caballos.DAO.apostante_DAO import ApostanteDAO
from carrera_caballos.DAO.caballos_DAO import CaballosDAO
from carrera_caballos.DAO.gran_premio_DAO import GranPremioDAO
from carrera_caballos.ficheros.read_apostantes import readapostantes
import logging

from carrera_caballos.ficheros.read_caballos import readcaballos
from carrera_caballos.ficheros.read_granpremio import readgrandespremios
from carrera_caballos.log import logging_caballo as logs

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def insertapostante():
    apostantes = readapostantes()
    for apostante in apostantes:
        ApostanteDAO.insertar(apostante)
        logs.info('apostante {} insertado'.format(apostante.nombre))


def insertcaballo():
    caballos = readcaballos()
    for caballo in caballos:
        CaballosDAO.insertar(caballo)
        logs.info('caballo {} insertado'.format(caballo.nombre))


def insertgranpremio():
    grandespremios = readgrandespremios()
    for granpremio in grandespremios:
        GranPremioDAO.insertar(granpremio)
        logs.info('gran premio {} insertado'.format(granpremio.nombre))
