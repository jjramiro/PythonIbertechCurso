from carrera_caballos.DAO.apostante_DAO import ApostanteDAO
from carrera_caballos.DAO.caballos_DAO import CaballosDAO
from insert_in_bbdd.insert_objects import insertgranpremio, insertcaballo, insertapostante
from log import logging_caballo as logs
import logging
from DAO.gran_premio_DAO import GranPremioDAO

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def mostrar_caballos(caballos):
    '''
    menu de caballos disponibles para apostar
    '''
    for caballo in caballos:
        print("{}. {} - {}".format(caballo.id, caballo.nombre, caballo.valor_apuesta))


def menu(caballos, apostante):
    '''
    funcion para mostrar los caballos disponibles y devolver el dinero y el caballo elegido
    '''
    logs.info('el apostante {} se dispone a entregar su dinero'.format(apostante.nombre))
    apuesta_no_valida = True
    while apuesta_no_valida:
        apuesta = input('cuanto quieres apostar? ')
        if int(apuesta) > apostante.saldo:
            logs.info('el apostante {} no tiene dinero suficiente, diga otra cantidad'.format(apostante.nombre))
        else:
            mostrar_caballos(caballos)
            caballo = input('porque caballo desea apostar? ')
            return apuesta, caballo


def comenzarapuestas(caballos, apostantes):
    '''
    funcion que devuelve el dinero de la apuesta junto con el caballo por el que se apuesta en un diccionario con el
    nombre del apostante para cada carrera
    '''
    apuestas = {}
    for apostante in apostantes:
        logs.info('entra en la casa de apuestas el apostante {}'.format(apostante.nombre))
        if apostante.saldo > 0:
            apuestafinal, caballoid = menu(caballos, apostante)
            apuestas[apostante.nombre] = [apuestafinal, caballoid]
            logs.info('el apostante {} ha finalizado su apuesta'.format(apostante.nombre))
        else:
            logs.info('el apostante {} no puede seguir apostando'.format(apostante.nombre))
    return apuestas


def iniciar_carrera(caballos):
    '''
    funcion para iniciar el calculo de cada carrera devolviendo el caballo ganador
    '''



def comenzarpremios(premios, caballos, apostantes):
    '''
    funcion para recorrer los premios de base de datos y entrar en el numero de carreras
    '''
    for premio in premios:
        logs.info('comienza el premio {}'.format(premio.nombre))
        carreras_hechas = 1
        while carreras_hechas <= premio.num_carreras:
            apuestas = comenzarapuestas(caballos, apostantes)
            logs.info('la carrera {} tiene las apuestas {}'.format(carreras_hechas, apuestas))
            ganador = iniciar_carrera(caballos)
            carreras_hechas += 1


if __name__ == '__main__':
    logs.info('comenzamos la casa de apuestas')
    # TODO: antes de subir a github descomentar lo de abajo
    '''insertgranpremio()
    insertcaballo()
    insertapostante()'''
    premios = GranPremioDAO.seleccionar()
    caballos = CaballosDAO.seleccionar()
    apostantes = ApostanteDAO.seleccionar()
    logs.debug(premios)
    comenzarpremios(premios, caballos, apostantes)
    logs.info('ha acabado la jornada de apuestas')

