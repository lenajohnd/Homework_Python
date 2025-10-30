from sqlalchemy import create_engine, text


class ScheduleTable:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        # Выносим все SQL-запросы в словарь
        self.queries = {
            "get_all": "SELECT * FROM subject",
            "find_by_id": "SELECT * FROM subject WHERE subject_id = :id",
            "delete": "DELETE FROM subject WHERE subject_id = :id",
            "insert": "INSERT INTO subject (subject_title) "
                      "VALUES (:title) RETURNING subject_id",
            "update": "UPDATE subject SET subject_title = :title "
                      "WHERE subject_id = :id"
        }

    # Получить все предметы
    def get_all_subjects(self):
        conn = self.engine.connect()
        result = conn.execute(text(self.queries["get_all"]))
        all_subjects = result.fetchall()
        conn.close()
        return all_subjects

    # Найти предмет по ID
    def find_subject_by_id(self, subject_id):
        conn = self.engine.connect()
        result = conn.execute(
            text(self.queries["find_by_id"]),
            {"id": subject_id}
        )
        subject = result.fetchall()
        conn.close()
        return subject

    # Удалить предмет
    def delete_subject(self, subject_id):
        conn = self.engine.connect()
        conn.execute(
            text(self.queries["delete"]),
            {"id": subject_id}
        )
        conn.commit()
        conn.close()

    # Добавить новый предмет
    def add_subject(self, subject_title):
        conn = self.engine.connect()
        result = conn.execute(
            text(self.queries["insert"]),
            {"title": subject_title}
        )
        conn.commit()
        new_id = result.fetchone()[0]
        conn.close()
        return new_id

    # Изменить предмет
    def change_subject(self, subject_id, new_title):
        conn = self.engine.connect()
        conn.execute(
            text(self.queries["update"]),
            {"id": subject_id, "title": new_title}
        )
        conn.commit()
        conn.close()
        return True
