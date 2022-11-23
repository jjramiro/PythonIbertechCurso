import os

from class_colegio import School, Student


def save_school(dic):
    for name in dic:
        file = open(name + '.txt', "w")
        for mate in dic[name].students:
            file.write(mate.name + '|' + mate.surname + '|' + mate.dni + '|' + mate.subjects)
        file.close()


if __name__ == '__main__':
    dic_school = {}
    with open('alumnos-colegio.txt', 'r', encoding='utf8') as rfile:
        for line in rfile.readlines():
            string_line = line.split('|')
            filename = string_line[0] + ".txt"
            if filename in os.listdir('./'):
                dic_school[string_line[0]].students.append(Student(string_line[1], string_line[2],
                                                                   string_line[3], string_line[4]))
            else:
                school = School(string_line[0])
                student = Student(string_line[1], string_line[2], string_line[3], string_line[4])
                school.students.append(student)
                dic_school[school.name] = school
            create_file = open(filename, "w")
            create_file.close()
        save_school(dic_school)
