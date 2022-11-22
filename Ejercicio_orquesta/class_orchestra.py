from abc import ABC
from random import randint

from decorator import orchestra_decorator
from orchestra_exceptions import TuneException
from utils import utils_tuned
from logging_general import log


class Orchestra:
    orchestra_list = []

    def create_orchestra(self):
        '''
            creamos los objetos de la orquesta y los añadimos a la lista de objetos del objeto orquesta
        '''
        log.info("empiezan a llegar los intrumentos de la orquesta")
        guitar = Guitar("guitarra", "cuerda", 5)
        electric_guitar = ElectricGuitar("guitarra electrica", "cuerda", 6, 80)
        piano = Piano("piano", "cuerda", 98)
        drum = Drum("bateria", "percusion", 70)
        self.orchestra_list = [guitar, electric_guitar, piano, drum]
        log.info("los instrumentos creados son: {}, {}, {} y {}".format(guitar.name, electric_guitar.name,
                                                                        piano.name, drum.name))

    def concert(self):
        '''
            para dar el concierto primero debemos afinar los intrumentos y por ultimo tocarlos para ver si estan bien
            afinados y se tocan correctamente si saltara un error
        '''
        for instrument in self.orchestra_list:
            instrument.tune()
        for tuned_instrument in self.orchestra_list:
            try:
                if tuned_instrument.kind == "percusion":
                    tuned_instrument.hammer(tuned_instrument.name)
                else:
                    tuned_instrument.play()
            except TuneException as e:
                log.error(e)


class Instrument(ABC):

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self._tuned = False

    @property
    def tuned(self):
        log.info("metodo getter activado")
        return self._tuned

    @tuned.setter
    def tuned(self, tuned_successful):
        log.info("metodo setter activado")
        self._tuned = tuned_successful


class Guitar(Instrument):

    def __init__(self, name, kind, string_num):
        Instrument.__init__(self, name, kind)
        self.string_num = string_num

    @orchestra_decorator
    def tune(self):
        if randint(1, 10) >= 5:
            self.tuned = True
            log.info("el instrumento {} se ha afinado correctamente".format(self.name))

    @orchestra_decorator
    def play(self):
        utils_tuned(self.tuned, self.name)


class ElectricGuitar(Guitar):

    def __init__(self, name, kind, string_num, power):
        Guitar.__init__(self, name, kind, string_num)
        self.power = power

    @orchestra_decorator
    def tune(self):
        if randint(1, 10) >= 5:
            self.tuned = True
            log.info("el instrumento {} se ha afinado correctamente".format(self.name))

    @orchestra_decorator
    def play(self):
        utils_tuned(self.tuned, self.name)


class Piano(Instrument):

    def __init__(self, name, kind, keynum):
        Instrument.__init__(self, name, kind)
        self.keynum = keynum

    @orchestra_decorator
    def tune(self):
        if randint(1, 10) >= 5:
            self.tuned = True
            log.info("el instrumento {} se ha afinado correctamente".format(self.name))

    @orchestra_decorator
    def play(self):
        utils_tuned(self.tuned, self.name)


class Drum(Instrument):

    def __init__(self, name, kind, size):
        Instrument.__init__(self, name, kind)
        self.size = size

    @orchestra_decorator
    def tune(self):
        if randint(1, 10) >= 5:
            self.tuned = True
            log.info("el instrumento {} se ha afinado correctamente".format(self.name))

    @orchestra_decorator
    def hammer(self, name):
        if self.tuned:
            print("Se esta tocando el tambor {}".format(name))
        else:
            raise TuneException('El instrumento {} no esta afinado'.format(self.name))
