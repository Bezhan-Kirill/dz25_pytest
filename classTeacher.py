class Teacher:

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_teacher_data(self):
        return f"{self.__name}, {self.__education}, опыт работы {self.__experience}"

    def add_mark(self, student, grade):
        return f"{self.__name} поставил оценку {grade} студенту {student}"

    def remove_mark(self, student, grade):
        return f"{self.__name} удалил оценку {grade} студенту {student}"

    def give_a_consultation(self, classroom):
        return f"{self.__name} провел консультацию в кабинете {classroom}"

    def get_name(self):
        return f'{self.__name}'

    def get_education(self):
        return f'{self.__education}'

    def get_experience(self):
        return f'{self.__experience}'

    def set_experience(self, experience):
        self.__experience = experience
