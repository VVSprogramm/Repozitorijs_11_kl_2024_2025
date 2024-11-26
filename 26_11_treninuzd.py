"""
Studentu klase
Uzdevums: Izveidot klasi Student, kas apraksta studentu ar šādām īpašībām un metodēm:
Īpašības:
name: studenta vārds.
student_id: studenta ID numurs.
grades: saraksts ar studenta iegūtajiem vērtējumiem.
Metodes:
add_grade(grade): pievieno jaunu vērtējumu sarakstam.
calculate_average(): aprēķina un atgriež studenta vidējo vērtējumu.
Papildu prasības:
Nodrošināt, ka vērtējums ir diapazonā no 0 līdz 10, un, ja tas tā nav, izvadīt kļūdas ziņojumu.

Izveido atbilstošu lietotāja grafisko saskrani (bilbiotēka PySimpeGUI vai kāds cits analogs)
"""
import PySimpleGUI as sg

class Student:
    # Īpašības:
    # name: studenta vārds.
    # student_id: studenta ID numurs.
    # grades: saraksts ar studenta iegūtajiem vērtējumiem.
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    # Metodes:
    # add_grade(grade): pievieno jaunu vērtējumu sarakstam.
    def add_grade(self, grade):
        # Papildu prasības:
        # Nodrošināt, ka vērtējums ir diapazonā no 0 līdz 10, un, ja tas tā nav, izvadīt kļūdas ziņojumu.
        if 0 <= grade <= 10:
            self.grades.append(grade)
            return f"Atzīme {grade} pievienota."
        else:
            return "Nederīga atzīme. Atzīmei jābūt starp 0 un 10."
    # Metodes:
    # calculate_average(): aprēķina un atgriež studenta vidējo vērtējumu.
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Pārbaude
student = Student("Anna Lapa", "12345")
print(student.add_grade(8))
print(student.add_grade(9))
print(student.add_grade(11))  # Nepareizs vērtējums
average = student.calculate_average()
print(f"{student.name} (ID: {student.student_id}) vidējā atzīme ir {average:.2f}.")


# GUI izkārtojums
layout = [
    [sg.Text("Skolēna vārds:"), sg.InputText(key="name")],
    [sg.Text("Skolēna ID:"), sg.InputText(key="student_id")],
    [sg.Button("Pievienot skolēnu")],
    [sg.Text("Izvēlēties skolēnu:"), sg.Combo([], size=(20, 1), key="student_select")],
    [sg.Text("Pievienot atzīmi:"), sg.InputText(key="grade"), sg.Button("Pievienot atzīmi")],
    [sg.Button("Aprēķināt vidējo")],
    [sg.Text("Rezultāts:", size=(40, 2), key="result")],
    [sg.Button("Iziet")]
]

# Loga izveide
window = sg.Window("Skolēnu dati", layout)

students = {}  # Saglabā studentus kā vārdnīcu: student_id -> Student objektu

while True:
    event, values = window.read()

    
    if event == sg.WINDOW_CLOSED or event == "Iziet":
        break
    
    if event == "Pievienot skolēnu":
        
        name = values["name"]
        student_id = values["student_id"]
        
        if name and student_id:
            if student_id not in students:
                students[student_id] = Student(name, student_id)
                window["student_select"].update(values=list(students.keys()))
                window["result"].update(f"Skolēns {name} pievienots!")
            else:
                window["result"].update("Skolēna ID jau eksistē.")
        else:
            window["result"].update("Lūdzu norādiet gan skolēna vārdu, gan ID.")
    
    if event == "Pievienot atzīmi":
        student_id = values["student_select"]
        if student_id:
            grade = values["grade"]
            try:
                grade = int(grade)
                result = students[student_id].add_grade(grade)
                window["result"].update(result)
            except ValueError:
                window["result"].update("Nepareiza atzīme. Lūdzu ievadi ciparu.")
        else:
            window["result"].update("Lūdzu izvēlies skolēnu.")
    
    if event == "Aprēķināt vidējo":
        student_id = values["student_select"]
        if student_id:
            avg = students[student_id].calculate_average()
            window["result"].update(f"Vidēja atzīme skolēnam: {students[student_id].name}: {avg:.2f}")
        else:
            window["result"].update("Lūdzu izvēlies skolēnu.")

window.close()
