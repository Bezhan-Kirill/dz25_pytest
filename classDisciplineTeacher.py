import classTeacher


class DisciplineTeacher(classTeacher.Teacher):
    teachers_list = []

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title
        DisciplineTeacher.teachers_list.append(self)

    def fire_teacher(self):
        if self in self.teachers_list:
            self.teachers_list.remove(self)
            return "Учитель был уволен!"
        else:
            return "Этот учитель уже был уволен!"

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        super().get_teacher_data()
        return f"Предмет: {self.__discipline}, должность {self.__job_title}"

    def add_mark(self, student, grade):
        super().add_mark(student, grade)
        return f"Предмет: {self.__discipline}"

    def remove_mark(self, student, grade):
        super().remove_mark(student, grade)
        print(f"Предмет: {self.__discipline}")

    def give_a_consultation(self, classroom):
        super().give_a_consultation(classroom)
        return f"По прeдмету {self.__discipline} как {self.__job_title}"


teacher1 = DisciplineTeacher("Иван Петров", "ДГТУ", "4 года", "Химия", "Директор")
teacher1.get_teacher_data()
teacher1.add_mark("Петр Сидоров", "4")
teacher1.remove_mark("Сергей Иванов", "3")
teacher1.give_a_consultation("9Б")

teacher2 = DisciplineTeacher("Татьяна Петрова", "ПТУ", "10 лет", "Английский", "Учитель")
teacher2.get_teacher_data()
teacher2.add_mark("Иван Сергеев", "5")
teacher2.remove_mark("Максим Алексев", "4")
teacher2.give_a_consultation("8А")

print(teacher1.fire_teacher())
print(teacher2.fire_teacher())
print(teacher2.fire_teacher())
