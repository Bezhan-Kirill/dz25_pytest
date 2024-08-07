from classTeacher import Teacher


def test_Teacher_init():
    teacher = Teacher('test_name', 'test_education', 'test_experience')


def test_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == "test_name, test_education, опыт работы test_experience"


def test_add_mark(teacher):
    assert teacher.add_mark("Иван Иванов", "5") == "test_name поставил оценку 5 студенту Иван Иванов"


def test_remove_mark(teacher):
    assert teacher.remove_mark("Иван Иванов", "5") == "test_name удалил оценку 5 студенту Иван Иванов"


def test_give_a_consultation(teacher):
    assert teacher.give_a_consultation("test_classroom") == "test_name провел консультацию в кабинете test_classroom"


def test_get_name(teacher):
    assert teacher.get_name() == "test_name"


def test_get_education(teacher):
    assert teacher.get_education() == "test_education"


def test_get_experience(teacher):
    assert teacher.get_experience() == "test_experience"


def test_set_experience(teacher):
    assert teacher.set_experience("test_experience") == None
