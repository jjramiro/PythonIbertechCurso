import logging
from Ejercicio1_basededatos.conexion import get_mysql_conection
from carrera_caballos.log import logging_caballo as logs
from carrera_caballos.clases.class_apostante import Apostante

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


class ApostanteDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM apostante ORDER BY id'
    _INSERTAR = 'INSERT INTO apostante(nombre, saldo) VALUES(%s, %s)'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                apostantes = []
                for registro in registros:
                    apostante = Apostante(registro[0], registro[1], registro[2])
                    apostantes.append(apostante)

                return apostantes

    @classmethod
    def insertar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                logs.info(f'productos insertada: {apostante}')
                return cursor.rowcount