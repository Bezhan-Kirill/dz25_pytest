from classDisciplineTeacher import DisciplineTeacher


def test_DisciplineTeacher_init():
    disciplineteacher = DisciplineTeacher('test_name', 'test_education', 'test_experience', 'test_discipline', 'test_job_title')
    assert len(DisciplineTeacher.teachers_list) == 1

def test_get_name(disciplineteacher):
    assert disciplineteacher.get_name() == "test_name"

def test_get_education(disciplineteacher):
    assert disciplineteacher.get_education() == "test_education"

def test_get_experience(disciplineteacher):
    assert disciplineteacher.get_experience() == "test_experience"

def test_get_discipline(disciplineteacher):
    assert disciplineteacher.get_discipline() == "test_discipline"

def test_get_job_title(disciplineteacher):
    assert disciplineteacher.get_job_title() == "test_job_title"

def test_set_job_title(disciplineteacher):
    assert disciplineteacher.set_job_title("test_job") == None

def test_get_teacher_data(disciplineteacher):
    assert disciplineteacher.get_teacher_data() == 'Предмет: test_discipline, должность test_job_title'

def test_add_mark(disciplineteacher):
    assert disciplineteacher.add_mark(4, "Иван Иванов") == "Предмет: test_discipline"

def test_remove_mark(disciplineteacher):
    assert disciplineteacher.add_mark(3, "Иван Иванов") == "Предмет: test_discipline"

def test_give_a_consultation(disciplineteacher):
    assert disciplineteacher.give_a_consultation("9Б") == "По прeдмету test_discipline как test_job_title"

def test_fire_teacher(disciplineteacher):
    assert disciplineteacher.fire_teacher() == "Учитель был уволен!"
    assert disciplineteacher.fire_teacher() == "Этот учитель уже был уволен!"