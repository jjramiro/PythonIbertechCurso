import logging
from Ejercicio1_basededatos.conexion import get_mysql_conection
from carrera_caballos.log import logging_caballo as logs
from carrera_caballos.clases.class_caballos import Caballo

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


class CaballosDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM caballos ORDER BY id'
    _INSERTAR = 'INSERT INTO caballos(nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta,' \
                'id_granpremio) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE caballos SET experiencia=%s WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballo = Caballo(registro[0], registro[1], registro[2], registro[3],
                                      registro[4], registro[5], registro[6])
                    caballos.append(caballo)

                return caballos

    @classmethod
    def insertar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad,
                           caballo.experiencia, caballo.valor_apuesta, caballo.id_granpremio)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                logs.info(f'productos insertada: {caballo}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, horse):
        if horse.experiencia >= 100:
            horse.experiencia = 100
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valor = (horse.experiencia, horse.id)
                cursor.execute(cls._ACTUALIZAR, valor)
                conexion.commit()
                logs.debug(f'productos actualizada: {horse}')
                return cursor.rowcount