from random import randint, choice


sick_rooms = []


class Hospital:

    def __init__(self, name):
        self.name = name

    def open(self):
        print("el hospital {} abre sus puertas".format(self.name))


class Human:

    def __init__(self, name, surname, dni):
        self.name = name
        self.surname = surname
        self.dni = dni


class Doctor(Human):

    def __init__(self, name, surname, dni, specialism):
        Human.__init__(self, name, surname, dni)
        self.specialism = specialism

    def sign_up(self):
        print("el doctor {} ha fichado su entrada".format(self.name))

    def diagnosticate(self, patient):
        diseases = ["cancer", "otitis", "gastroenteritis", "escorbuto"]
        if randint(1, 10) > 7 and len(sick_rooms) < 3:
            sick = Sick(patient.name, patient.surname, patient.dni, choice(diseases))
            print("el doctor {} ha mandado al paciente {} a ingresar por {}".format(self.name, patient.name, sick.disease))
            sick_rooms.append(sick)
            print("en ingresos hay {} enfermos".format(len(sick_rooms)))
        elif len(sick_rooms) >= 3:
            print("el doctor {} ha mandado al paciente {} a el hospital vecino oro jackson".format(self.name,
                                                                                                   patient.name))
        else:
            print("el doctor {} ha mandado al paciente {} a casa a descansar".format(self.name, patient.name))


class Nurse(Human):

    def __init__(self, name, surname, dni, floor):
        Human.__init__(self, name, surname, dni)
        self.floor = floor

    def sign_up(self):
        print("el enfermer@ {} ha fichado su entrada".format(self.name))

    def care(self, patient, room):
        room.patient = patient
        room.entry()


class Patient(Human):

    def __init__(self, name, surname, dni, symptom):
        Human.__init__(self, name, surname, dni)
        self.symptom = symptom


class Sick(Human):

    def __init__(self, name, surname, dni, disease):
        Human.__init__(self, name, surname, dni)
        self.disease = disease


class Room:

    def __init__(self, name, doctor, patient=None):
        self.name = name
        self.doctor = doctor
        self.patient = patient

    def entry(self):
        print("el paciente {} ha entrado en la consulta {} a cargo del doctor {}".format(self.patient.name, self.name,
                                                                                         self.doctor.name))
        self.doctor.diagnosticate(self.patient)