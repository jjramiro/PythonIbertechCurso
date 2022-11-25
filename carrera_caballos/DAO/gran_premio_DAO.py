import logging
from Ejercicio1_basededatos.conexion import get_mysql_conection
from carrera_caballos.log import logging_caballo as logs
from carrera_caballos.clases.class_gran_premio import GranPremio

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


class GranPremioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM gran_premio ORDER BY id'
    _INSERTAR = 'INSERT INTO gran_premio(nombre, distancia, num_carreras) VALUES(%s, %s, %s)'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                premios = []
                for registro in registros:
                    premio = GranPremio(registro[0], registro[1], registro[2], registro[3])
                    premios.append(premio)

                return premios

    @classmethod
    def insertar(cls, premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (premio.nombre, premio.distancia, premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                logs.info(f'productos insertada: {premio}')
                return cursor.rowcount
