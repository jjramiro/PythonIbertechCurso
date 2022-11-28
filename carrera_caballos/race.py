from carrera_caballos.DAO.apostante_DAO import ApostanteDAO
from carrera_caballos.DAO.caballos_DAO import CaballosDAO
from insert_in_bbdd.insert_objects import insertgranpremio, insertcaballo, insertapostante
from log import logging_caballo as logs
import logging
from DAO.gran_premio_DAO import GranPremioDAO

logs.setupLogging(logging.DEBUG, "../carrera_caballos/log/caballos.log")


def mostrar_caballos(caballos, idpremio):
    '''
    menu de caballos disponibles para apostar
    '''
    for caballo in caballos:
        if caballo.id_granpremio == idpremio:
            print("{}. {} - {}".format(caballo.id, caballo.nombre, caballo.valor_apuesta))


def menu(caballos, apostante, idpremio):
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
            mostrar_caballos(caballos, idpremio)
            caballo = input('porque caballo desea apostar? ')
            return apuesta, caballo


def comenzarapuestas(caballos, apostantes, idpremio):
    '''
    funcion que devuelve el dinero de la apuesta junto con el caballo por el que se apuesta en un diccionario con el
    nombre del apostante para cada carrera
    '''
    apuestas = {}
    for apostante in apostantes:
        logs.info('entra en la casa de apuestas el apostante {}'.format(apostante.nombre))
        if apostante.saldo > 0:
            apuestafinal, caballoid = menu(caballos, apostante, idpremio)
            apuestas[apostante.nombre] = [apuestafinal, caballoid]
            logs.info('el apostante {} ha finalizado su apuesta'.format(apostante.nombre))
        else:
            logs.info('el apostante {} no puede seguir apostando'.format(apostante.nombre))
    return apuestas


def iniciar_carrera(caballos, premio):
    '''
    funcion para iniciar el calculo de cada carrera devolviendo el caballo ganador
    '''
    winer = caballos[0]
    while winer.distancia < premio.distancia:
        for caballo in caballos:
            if caballo.id_granpremio == premio.id:
                caballo.run()
                if caballo.distancia > winer.distancia:
                    winer = caballo
                logs.info("el caballo {} va ganado".format(winer.nombre))
    for caballo in caballos:
        caballo.distancia = 0
    return winer


def cambio_saldo(winer, bets, bettors):
    for bettor in bettors:
        logs.info("el apostante {} comienza con un saldo de {}".format(bettor.nombre, bettor.saldo))
        apuesta = bets[bettor.nombre]
        if int(apuesta[1]) == int(winer.id):
            bettor.saldo += int(apuesta[0]) * int(winer.valor_apuesta)
        else:
            bettor.saldo += -(int(apuesta[0]))
        logs.info("el apostante {} termina con un saldo de {}".format(bettor.nombre, bettor.saldo))
    return bettors


def ganar_experiencia(horses, winer, idpremio):
    for horse in horses:
        if horse.id_granpremio == idpremio:
            if horse.id == winer.id:
                horse.experiencia += 5
            else:
                horse.experiencia += 1
            CaballosDAO.actualizar(horse)
    return horses


def resumen_apostantes(apostantes):
    for apostante in apostantes:
        logs.info('el apostante {} ha acabado la carrera con un saldo de {}'.format(apostante.nombre, apostante.saldo))


def comenzarpremios(premios, caballos, apostantes):
    '''
    funcion para recorrer los premios de base de datos y entrar en el numero de carreras
    '''
    for premio in premios:
        logs.info('comienza el premio {}'.format(premio.nombre))
        carreras_hechas = 1
        while carreras_hechas <= premio.num_carreras:
            apuestas = comenzarapuestas(caballos, apostantes, premio.id)
            logs.info('la carrera {} tiene las apuestas {}'.format(carreras_hechas, apuestas))
            ganador = iniciar_carrera(caballos, premio)
            apostantes = cambio_saldo(ganador, apuestas, apostantes)
            caballos = ganar_experiencia(caballos, ganador, premio.id)
            resumen_apostantes(apostantes)
            carreras_hechas += 1


if __name__ == '__main__':
    logs.info('comenzamos la casa de apuestas')
    insertgranpremio()
    insertcaballo()
    insertapostante()
    premios = GranPremioDAO.seleccionar()
    caballos = CaballosDAO.seleccionar()
    apostantes = ApostanteDAO.seleccionar()
    logs.debug(premios)
    comenzarpremios(premios, caballos, apostantes)
    logs.info('ha acabado la jornada de apuestas')

