import sys
from typing import Optional

import PySide6.QtCore
import PySide6.QtWidgets
from ui_Interfacepro import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None) :
        super().__init__()
        self.setupUi(self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())