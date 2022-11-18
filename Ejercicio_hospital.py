from clases_hospital import Hospital, Doctor, Nurse, Room, Patient
from utils import sign

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
    hospital.open()
    sign(doctor1, doctor2, nurse1, nurse2)
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