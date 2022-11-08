import sqlite3


class DataBase:

    def __init__(self, database_path):
        self._database = sqlite3.connect(database_path)
        self._cursor = self._database.cursor()
        self._make_db()

    def _make_db(self):
        self._cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                             'question1 INTEGER REFERENCES answers(id), question2 INTEGER REFERENCES answers(id), '
                             'question3 INTEGER REFERENCES answers(id), question4 INTEGER REFERENCES answers(id),'
                             'question5 INTEGER REFERENCES answers(id), question6 INTEGER REFERENCES answers(id),'
                             'question7 INTEGER REFERENCES answers(id), question8 INTEGER REFERENCES answers(id),'
                             'question9 INTEGER REFERENCES answers(id))')
        self._cursor.execute('CREATE TABLE IF NOT EXISTS answers (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                             'answer TEXT)')
        self._cursor.execute("SELECT * FROM answers")
        if not self._cursor.fetchall():
            self._cursor.execute("INSERT INTO answers (answer)"
                                 "VALUES ('Да'), ('Нет'), ('Мужской'), ('Женский')")
        self._database.commit()

    def add(self, info: dict):
        self._cursor.execute("INSERT INTO users (question1, question2, question3, question4, question5, question6, "
                             "question7, question8, question9)"
                             "VALUES ((SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?), "
                             "(SELECT id FROM answers WHERE answer = ?))",
                             (info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9]))
        self._database.commit()

    def target_from_db(self):
        self._cursor.execute("SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question1 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question2 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question3 = answers.id "
                             "WHERE users.question2 IN (SELECT my_id FROM "
                             "(SELECT MAX(my_count), my_id FROM "
                             "(SELECT answers.id AS my_id, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question2 = answers.id "
                             "GROUP BY my_id))) "
                             "GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question4 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question5 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question6 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question7 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question8 = answers.id GROUP BY answers.answer) "
                             
                             "UNION ALL "
                             "SELECT MAX(my_count), answer FROM "
                             "(SELECT answers.answer AS answer, COUNT(answers.answer) AS my_count "
                             "FROM users INNER JOIN answers ON users.question9 = answers.id GROUP BY answers.answer) "
                             )
        return self._cursor.fetchall()
