import pytest
from classTeacher import Teacher
from classDisciplineTeacher import DisciplineTeacher


@pytest.fixture
def teacher():
    teacher = Teacher('test_name', 'test_education', 'test_experience')
    return teacher


@pytest.fixture
def disciplineteacher():
    DisciplineTeacher.teachers_list.clear()
    disciplineteacher = DisciplineTeacher('test_name', 'test_education', 'test_experience', 'test_discipline', 'test_job_title')
    return disciplineteacher