import random
from utils.format_text import format_text

name_students = ["Ana", "Bruno", "Carlos", "Diana", "Edson"]
room_students = ["Sala 1", "Sala 2", "Sala 3"]

def aloc_students(name_list, class_list):
    random_name_student = random.choice(name_list)
    random_room_students = random.choice(class_list)

    name_student_formated = format_text(random_name_student)

    dictionary_class = {
        "Nome": name_student_formated,
        "Sala": random_room_students
    }

    return dictionary_class

aloc_students(name_students, room_students)