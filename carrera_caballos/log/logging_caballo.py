import logging as log


def setupLogging(logLevel, filePath):
    log.basicConfig(level=logLevel,
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        log.FileHandler(filePath),
                        log.StreamHandler()
                    ])


def debug(*message):
    log.debug(genera_mensaje(message))


def info(*message):
    log.info(message)


def warn(*message):
    log.warning(message)


def error(*message):
    log.error(message)


def critical(*message):
    log.critical(message)


def genera_mensaje(mensajes):
    reply = ""
    for mensaje in mensajes:
        reply += str(mensaje)

    return reply