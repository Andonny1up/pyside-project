import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase, QSqlQuery

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(absPath("contact.db"))

if not connection.open():
    print("No se puede conectart a la db")
    sys.exit(True)

query = QSqlQuery()
query.exec("DROP TABLE IF EXISTS contacts")
query.exec("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
""")

name,job,email = "Hector","Instructor","Hectoraso@email.com"

query.exec(f"""
    INSERT INTO contacts (name,job,email)
    VALUES ('{name}','{job}','{email}')
""")

contacts = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

query.prepare("INSERT INTO contacts (name,job,email) VALUES (?,?,?)")

for name, job, email in contacts:
    query.addBindValue(name)
    query.addBindValue(job)
    query.addBindValue(email)
    query.exec()

query.exec("SELECT name,job,email FROM contacts")

# if query.first():
#     print(query.value("name"))

while query.next():
    print(query.value("name"),query.value("job"),query.value("email"))

connection.close()
print("Conexion cerrada?", not connection.isOpen())