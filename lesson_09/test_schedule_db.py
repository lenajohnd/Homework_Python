import time
from ScheduleTable import ScheduleTable

db = ScheduleTable("postgresql://user:password@localhost:5432/названиеБД")
# Подставляйте сами


# Тест 1: Добавление предмета
def test_add_subject():
    current_time = str(int(time.time()))
    subject_name = "Математика_" + current_time

    new_id = db.add_subject(subject_name)
    found_subjects = db.find_subject_by_id(new_id)

    assert len(found_subjects) == 1
    assert found_subjects[0].subject_title == subject_name

    db.delete_subject(new_id)


# Тест 2: Изменение предмета
def test_change_subject():
    current_time = str(int(time.time()))
    old_name = "Физика_" + current_time
    new_name = "Химия_" + current_time

    subject_id = db.add_subject(old_name)
    db.change_subject(subject_id, new_name)
    updated_subject = db.find_subject_by_id(subject_id)

    assert updated_subject[0].subject_title == new_name

    db.delete_subject(subject_id)


# Тест 3: Удаление предмета
def test_delete_subject():
    current_time = str(int(time.time()))
    subject_name = "Биология_" + current_time

    subject_id = db.add_subject(subject_name)
    db.delete_subject(subject_id)

    result = db.find_subject_by_id(subject_id)
    assert len(result) == 0
