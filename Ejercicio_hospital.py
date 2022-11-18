from random import randint, choice


class Hospital:

    def __init__(self, name):
        self.name = name

    def open(self):
        print("el hospital {} abre sus puertas".format(self.name))
        doctor1.sign_up()
        doctor2.sign_up()
        nurse1.sign_up()
        nurse2.sign_up()


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


if __name__ == '__main__':
    # creación de objetos
    hospital = Hospital("Moby_Dick")
    doctor1 = Doctor("Law", "Trafalgar", "12345678L", "Neurocirugía")
    doctor2 = Doctor("Marco", "Phoenix", "87654321M", "Geriatría")
    nurse1 = Nurse("Chopper", "Tony Tony", "75369124C", "primera planta")
    nurse2 = Nurse("Crocus", "Laboon", "85264739C", "segunda planta")
    room1 = Room("consulta 1", doctor1)
    room2 = Room("consulta 2", doctor2)
    patient1 = Patient("zoro", "Roronoa", "12654789Z", "mareos")
    patient2 = Patient("Edward", "Newgate", "45632178S", "taquicardia")
    patient3 = Patient("Ace", "Portgas", "78965432A", "dolor de pecho")
    patient4 = Patient("Sanji", "Vinsmoke", "63254178V", "ahogos")
    lobby = [patient1, patient2, patient3, patient4]
    sick_rooms = []
    hospital.open()
    entry_ticket = 0
    while len(lobby) > 0:
        if entry_ticket % 2 == 0:
            print("el enfermero {} esta atendiendo al paciente {}".format(nurse2.name, lobby[0].name))
            nurse2.care(lobby[0], room1)
        else:
            print("el enfermero {} esta atendiendo al paciente {}".format(nurse1.name, lobby[0].name))
            nurse1.care(lobby[0], room2)
        entry_ticket += 1
        lobby.pop(0)
    print("el hospital ha cerrado sus puertas")