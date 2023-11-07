import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # nos conectamos a la base de datos
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("contactos.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        # creamos el modelo
        self.modelo = QSqlTableModel()
        self.modelo.setTable("contactos")
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # configuramos la tabla
        self.tabla.setModel(self.modelo)
        self.tabla.resizeColumnsToContents()
        self.tabla.setColumnHidden(0, True)

        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tabla.selectionModel().selectionChanged.connect(self.select_row)
        self.boton_modificar.clicked.connect(self.edit_row)
        self.boton_nuevo.clicked.connect(self.new_row)
        self.boton_borrar.clicked.connect(self.destroy_row)

        self.row = -1

    def select_row(self,selecction):
        if selecction.indexes():
            self.row = selecction.indexes()[0].row()
            name = self.modelo.index(self.row, 1).data()
            job = self.modelo.index(self.row, 2).data()
            email = self.modelo.index(self.row, 3).data()
            self.line_nombre.setText(name)
            self.line_empleo.setText(job)
            self.line_email.setText(email)

    def edit_row(self):
        name = self.line_nombre.text()
        job = self.line_empleo.text()
        email = self.line_email.text()

        self.modelo.setData(self.modelo.index(self.row, 1), name)
        self.modelo.setData(self.modelo.index(self.row, 2), job)
        self.modelo.setData(self.modelo.index(self.row, 3), email)
        self.modelo.submit()


    def new_row(self):
        name = self.line_nombre.text()
        job = self.line_empleo.text()
        email = self.line_email.text()

        if len(name) > 0 and len(job) > 0 and len(email) > 0:
            index_row = self.modelo.rowCount()
            self.modelo.insertRow(index_row)
            self.modelo.setData(self.modelo.index(index_row, 1), name)
            self.modelo.setData(self.modelo.index(index_row, 2), job)
            self.modelo.setData(self.modelo.index(index_row, 3), email)
            self.modelo.submit()

            self.line_nombre.setText("")
            self.line_empleo.setText("")
            self.line_email.setText("")


    def destroy_row(self):
        if self.row >= 0:
            self.modelo.removeRow(self.row)
            self.modelo.select()
            self.row = -1

            self.line_nombre.setText("")
            self.line_empleo.setText("")
            self.line_email.setText("")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
